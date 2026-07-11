"""EBIOS-RM-flavored risk linking: feared_events + risk FK columns

Revision ID: 202607130001
Revises: 202607120001
Create Date: 2026-07-13 00:01:00

Extends the risk model with the "asset-value / threat-source /
feared-events structure" docs/roadmap.md's EBIOS RM item names -- NOT the
full 5-workshop ANSSI EBIOS RM methodology (no risk-source/target-objective
pairing, no attack-path scenarios, no treatment workflow). See
docs/roadmap.md for exactly what this is and isn't.

Adds a new `feared_events` table (a feared event conflates EBIOS RM's
"business value" and "supporting asset" tiers into the existing `assets`
CMDB table, stated as a deliberate simplification) and 4 nullable FK
columns on the pre-existing `risks` table: `asset_id`, `threat_id`,
`vulnerability_id`, `feared_event_id`. `feared_events` must be created
*before* `risks` gets its `feared_event_id` FK constraint added, since that
constraint references it -- hence `_create_feared_events_table()` runs
before `_add_risk_link_columns()` in `upgrade()`.

`feared_events.asset_id` is NOT NULL with `ondelete="RESTRICT"` (a feared
event with no asset is meaningless in EBIOS RM, and there's no legacy-row
backfill problem forcing it nullable, unlike risks' 4 new columns) --
mirrors the existing `Assessment.framework_version_id`/
`AssessmentResult.framework_version_id` precedent in
`compliance/models.py`, both NOT NULL FKs to a shared reference entity using
`ondelete="RESTRICT"`. Costs nothing since this app never hard-deletes
assets in its own code paths (only soft-deletes via `deleted_at`).

Follows `202607120001`'s idempotent permission-seeding pattern for the 2 new
`feared_events:*` codes -- see that migration's docstring (and
`202607100002` before it) for why blind inserts are unsafe.
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607130001"
down_revision: str | None = "202607120001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSIONS: dict[str, str] = {
    "feared_events:read": "View feared events",
    "feared_events:manage": "Create feared events",
}

ROLE_GRANTS: dict[str, tuple[str, ...]] = {
    "Admin": tuple(PERMISSIONS.keys()),
    "Manager": tuple(PERMISSIONS.keys()),
    "Auditor": ("feared_events:read",),
    "Viewer": ("feared_events:read",),
}


def _permissions_table() -> sa.Table:
    return sa.table(
        "permissions",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
        sa.column("description", sa.String),
        sa.column("created_at", sa.DateTime(timezone=True)),
        sa.column("updated_at", sa.DateTime(timezone=True)),
    )


def _role_permissions_table() -> sa.Table:
    return sa.table(
        "role_permissions",
        sa.column("role_id", postgresql.UUID(as_uuid=True)),
        sa.column("permission_id", postgresql.UUID(as_uuid=True)),
    )


def _roles_table() -> sa.Table:
    return sa.table(
        "roles",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("organization_id", postgresql.UUID(as_uuid=True)),
        sa.column("name", sa.String),
        sa.column("is_system", sa.Boolean),
    )


def _create_feared_events_table() -> None:
    criterion = postgresql.ENUM(
        "CONFIDENTIALITY", "INTEGRITY", "AVAILABILITY", name="fearedeventcriterion", create_type=False
    )
    gravity = postgresql.ENUM(
        "LOW", "MEDIUM", "HIGH", "CRITICAL", name="fearedeventgravity", create_type=False
    )
    for enum in (criterion, gravity):
        enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "feared_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("asset_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("criterion", criterion, nullable=False),
        sa.Column("gravity", gravity, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_feared_events_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["asset_id"], ["assets.id"], name="fk_feared_events_asset_id_assets", ondelete="RESTRICT"
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_feared_events_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_feared_events_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_feared_events"),
    )
    op.create_index("ix_feared_events_organization_id", "feared_events", ["organization_id"])
    op.create_index("ix_feared_events_asset_id", "feared_events", ["asset_id"])


def _add_risk_link_columns() -> None:
    for column_name, referent_table in (
        ("asset_id", "assets"),
        ("threat_id", "threats"),
        ("vulnerability_id", "vulnerabilities"),
        ("feared_event_id", "feared_events"),
    ):
        op.add_column("risks", sa.Column(column_name, postgresql.UUID(as_uuid=True), nullable=True))
        op.create_foreign_key(
            f"fk_risks_{column_name}_{referent_table}",
            "risks", referent_table, [column_name], ["id"], ondelete="SET NULL",
        )
        op.create_index(f"ix_risks_{column_name}", "risks", [column_name])


def _seed_permissions_and_grants() -> None:
    if context.is_offline_mode():
        return
    bind = op.get_bind()
    permissions = _permissions_table()
    role_permissions = _role_permissions_table()
    roles = _roles_table()
    now = datetime.now(UTC)

    permission_ids: dict[str, object] = {}
    for code, description in PERMISSIONS.items():
        permission_id = bind.execute(
            sa.select(permissions.c.id).where(permissions.c.code == code)
        ).scalar_one_or_none()
        if permission_id is None:
            permission_id = uuid4()
            op.bulk_insert(
                permissions,
                [
                    {
                        "id": permission_id,
                        "code": code,
                        "description": description,
                        "created_at": now,
                        "updated_at": now,
                    }
                ],
            )
        permission_ids[code] = permission_id

    for role_name, codes in ROLE_GRANTS.items():
        role_id = bind.execute(
            sa.select(roles.c.id).where(
                sa.and_(
                    roles.c.name == role_name,
                    roles.c.organization_id.is_(None),
                    roles.c.is_system.is_(True),
                )
            )
        ).scalar_one_or_none()
        if role_id is None:
            continue

        for code in codes:
            permission_id = permission_ids[code]
            already_granted = bind.execute(
                sa.select(role_permissions.c.role_id).where(
                    sa.and_(
                        role_permissions.c.role_id == role_id,
                        role_permissions.c.permission_id == permission_id,
                    )
                )
            ).scalar_one_or_none()
            if already_granted is None:
                op.bulk_insert(
                    role_permissions,
                    [{"role_id": role_id, "permission_id": permission_id}],
                )


def upgrade() -> None:
    _create_feared_events_table()
    _add_risk_link_columns()
    _seed_permissions_and_grants()


def downgrade() -> None:
    if not context.is_offline_mode():
        bind = op.get_bind()
        permissions = _permissions_table()
        role_permissions = _role_permissions_table()
        for code in PERMISSIONS:
            permission_id = bind.execute(
                sa.select(permissions.c.id).where(permissions.c.code == code)
            ).scalar_one_or_none()
            if permission_id is not None:
                op.execute(role_permissions.delete().where(role_permissions.c.permission_id == permission_id))
                op.execute(permissions.delete().where(permissions.c.id == permission_id))

    # Reverse of the tuple list in _add_risk_link_columns().
    for column_name, referent_table in (
        ("feared_event_id", "feared_events"),
        ("vulnerability_id", "vulnerabilities"),
        ("threat_id", "threats"),
        ("asset_id", "assets"),
    ):
        op.drop_index(f"ix_risks_{column_name}", table_name="risks")
        op.drop_constraint(f"fk_risks_{column_name}_{referent_table}", "risks", type_="foreignkey")
        op.drop_column("risks", column_name)

    op.drop_index("ix_feared_events_asset_id", table_name="feared_events")
    op.drop_index("ix_feared_events_organization_id", table_name="feared_events")
    op.drop_table("feared_events")
    for name in ("fearedeventgravity", "fearedeventcriterion"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
