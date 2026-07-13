"""EBIOS RM Workshop 2: risk sources + risk origins (SR/OV pairing)

Revision ID: 202607150001
Revises: 202607140001
Create Date: 2026-07-15 00:01:00

The full 5-workshop ANSSI EBIOS RM methodology has, until now, only had its
Workshop-1-adjacent structural linking done (asset/threat/vulnerability/
feared-event -- see 202607130001). This migration adds Workshop 2: "sources
de risque / objectifs vises" (risk sources and their target objectives).

Two new tables:

`risk_sources` -- a standalone catalog (mirrors `threats`'s shape) of threat
actors, scored on ANSSI's standard 3 axes: `category` (the 7 official ANSSI
risk-source categories: state, organized crime, terrorist, activist,
vengeful individual, amateur, specialized firm), `motivation` and
`resources` (a shared 4-level scale ANSSI's Workshop 2 grid uses for both),
and `activity` (a simpler 3-level scale for how actively this actor type is
currently observed operating).

`risk_origins` -- the actual "couple SR/OV" (risk-source / target-objective
pair): links a `risk_source_id` (mandatory -- a RiskOrigin *is* the pairing,
so this can never be null, unlike `feared_event_id` which is optional since
not every objective maps to a pre-existing feared event) to a free-text
`target_objective`, scored for `pertinence` (a 4-level scale reusing
`feared_events.gravity`'s shape) and flagged `retained` for whether this
pair is prioritized to carry forward into Workshop 3's strategic scenarios
(not built here -- see docs/roadmap.md for exactly what is and isn't
covered).

`risk_sources` must be created before `risk_origins`, whose
`risk_source_id` FK references it -- same ordering constraint
202607130001 established for `feared_events`/`risks`.

Follows the idempotent permission-seeding pattern established by
202607120001 onward for the 4 new `risk_sources:*`/`risk_origins:*` codes.
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607150001"
down_revision: str | None = "202607140001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSIONS: dict[str, str] = {
    "risk_sources:read": "View the EBIOS RM risk source catalog",
    "risk_sources:manage": "Create risk sources",
    "risk_origins:read": "View EBIOS RM risk origin (SR/OV) pairs",
    "risk_origins:manage": "Create and prioritize risk origin (SR/OV) pairs",
}

ROLE_GRANTS: dict[str, tuple[str, ...]] = {
    "Admin": tuple(PERMISSIONS.keys()),
    "Manager": tuple(PERMISSIONS.keys()),
    "Auditor": ("risk_sources:read", "risk_origins:read"),
    "Viewer": ("risk_sources:read", "risk_origins:read"),
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


def _create_risk_sources_table() -> None:
    category = postgresql.ENUM(
        "STATE",
        "ORGANIZED_CRIME",
        "TERRORIST",
        "ACTIVIST",
        "VENGEFUL_INDIVIDUAL",
        "AMATEUR",
        "SPECIALIZED_FIRM",
        name="risksourcecategory",
        create_type=False,
    )
    level = postgresql.ENUM(
        "LOW", "MODERATE", "SIGNIFICANT", "VERY_HIGH", name="risksourcelevel", create_type=False
    )
    activity = postgresql.ENUM("LOW", "MEDIUM", "HIGH", name="risksourceactivity", create_type=False)
    for enum in (category, level, activity):
        enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "risk_sources",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("category", category, nullable=False),
        sa.Column("motivation", level, nullable=False),
        sa.Column("resources", level, nullable=False),
        sa.Column("activity", activity, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_risk_sources_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_risk_sources_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_risk_sources_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_risk_sources"),
    )
    op.create_index("ix_risk_sources_organization_id", "risk_sources", ["organization_id"])


def _create_risk_origins_table() -> None:
    pertinence = postgresql.ENUM(
        "LOW", "MEDIUM", "HIGH", "CRITICAL", name="riskoriginpertinence", create_type=False
    )
    pertinence.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "risk_origins",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("risk_source_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("target_objective", sa.Text(), nullable=False),
        sa.Column("feared_event_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("pertinence", pertinence, nullable=False),
        sa.Column("retained", sa.Boolean(), nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_risk_origins_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["risk_source_id"], ["risk_sources.id"], name="fk_risk_origins_risk_source_id_risk_sources",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["feared_event_id"], ["feared_events.id"], name="fk_risk_origins_feared_event_id_feared_events",
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_risk_origins_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_risk_origins_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_risk_origins"),
    )
    op.create_index("ix_risk_origins_organization_id", "risk_origins", ["organization_id"])
    op.create_index("ix_risk_origins_risk_source_id", "risk_origins", ["risk_source_id"])
    op.create_index("ix_risk_origins_feared_event_id", "risk_origins", ["feared_event_id"])


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
    _create_risk_sources_table()
    _create_risk_origins_table()
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

    op.drop_index("ix_risk_origins_feared_event_id", table_name="risk_origins")
    op.drop_index("ix_risk_origins_risk_source_id", table_name="risk_origins")
    op.drop_index("ix_risk_origins_organization_id", table_name="risk_origins")
    op.drop_table("risk_origins")
    postgresql.ENUM(name="riskoriginpertinence").drop(op.get_bind(), checkfirst=True)

    op.drop_index("ix_risk_sources_organization_id", table_name="risk_sources")
    op.drop_table("risk_sources")
    for name in ("risksourceactivity", "risksourcelevel", "risksourcecategory"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
