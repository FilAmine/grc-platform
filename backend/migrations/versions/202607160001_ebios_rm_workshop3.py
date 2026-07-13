"""EBIOS RM Workshop 3: ecosystem parties + strategic scenarios

Revision ID: 202607160001
Revises: 202607150001
Create Date: 2026-07-16 00:01:00

Workshop 2 (202607150001) added risk sources and the SR/OV pairing. This
migration adds Workshop 3: mapping the ecosystem (third parties an attack
path could use as a stepping stone) and building strategic scenarios that
elaborate a *retained* SR/OV pair into a concrete attack path targeting a
specific feared event.

Two new tables:

`ecosystem_parties` -- a standalone catalog (mirrors `risk_sources`'s
shape) of suppliers/subcontractors/partners/clients, each scored on
`dependency_level` (how critical to this org's own operations) and
`cyber_maturity` (their own security posture -- low maturity makes a party
a more attractive stepping stone), both sharing a 3-level scale.

`strategic_scenarios` -- the actual Workshop 3 output. `risk_origin_id` and
`feared_event_id` are both mandatory FKs (`ondelete="RESTRICT"`): a
strategic scenario *is* the elaboration of a specific SR/OV pair targeting
a specific feared event, so neither can go null without the row losing its
meaning -- same reasoning `202607150001` used for `risk_origins.risk_source_id`.
`ecosystem_party_id` is optional (`ondelete="SET NULL"`): not every attack
path routes through a third party. Severity is deliberately not stored on
this table -- it's read off the required `feared_event_id` link's
`gravity` rather than copied, avoiding a second source of truth.

`ecosystem_parties` must be created before `strategic_scenarios`, whose
`ecosystem_party_id` FK references it -- same ordering constraint every
prior EBIOS RM migration in this repo has followed.

The API layer (not this migration) additionally enforces that a strategic
scenario can only be built from a `risk_origins` row with `retained=True`
-- a methodological check, not a schema one, so it isn't a DB constraint
here.

Follows the idempotent permission-seeding pattern established by
202607120001 onward for the 4 new `ecosystem_parties:*`/
`strategic_scenarios:*` codes.
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607160001"
down_revision: str | None = "202607150001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSIONS: dict[str, str] = {
    "ecosystem_parties:read": "View the EBIOS RM ecosystem party catalog",
    "ecosystem_parties:manage": "Create ecosystem parties",
    "strategic_scenarios:read": "View EBIOS RM strategic scenarios",
    "strategic_scenarios:manage": "Create strategic scenarios",
}

ROLE_GRANTS: dict[str, tuple[str, ...]] = {
    "Admin": tuple(PERMISSIONS.keys()),
    "Manager": tuple(PERMISSIONS.keys()),
    "Auditor": ("ecosystem_parties:read", "strategic_scenarios:read"),
    "Viewer": ("ecosystem_parties:read", "strategic_scenarios:read"),
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


def _create_ecosystem_parties_table() -> None:
    category = postgresql.ENUM(
        "PROVIDER", "SUBCONTRACTOR", "PARTNER", "CLIENT", name="ecosystempartycategory", create_type=False
    )
    level = postgresql.ENUM("LOW", "MEDIUM", "HIGH", name="ecosystempartylevel", create_type=False)
    for enum in (category, level):
        enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "ecosystem_parties",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("category", category, nullable=False),
        sa.Column("dependency_level", level, nullable=False),
        sa.Column("cyber_maturity", level, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_ecosystem_parties_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_ecosystem_parties_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_ecosystem_parties_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_ecosystem_parties"),
    )
    op.create_index("ix_ecosystem_parties_organization_id", "ecosystem_parties", ["organization_id"])


def _create_strategic_scenarios_table() -> None:
    likelihood = postgresql.ENUM(
        "LOW", "MEDIUM", "HIGH", "CRITICAL", name="strategicscenariolikelihood", create_type=False
    )
    likelihood.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "strategic_scenarios",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("risk_origin_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("feared_event_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("ecosystem_party_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("likelihood", likelihood, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"],
            name="fk_strategic_scenarios_organization_id_organizations", ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["risk_origin_id"], ["risk_origins.id"],
            name="fk_strategic_scenarios_risk_origin_id_risk_origins", ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["feared_event_id"], ["feared_events.id"],
            name="fk_strategic_scenarios_feared_event_id_feared_events", ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["ecosystem_party_id"], ["ecosystem_parties.id"],
            name="fk_strategic_scenarios_ecosystem_party_id_ecosystem_parties", ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_strategic_scenarios_created_by_id_users",
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_strategic_scenarios_updated_by_id_users",
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_strategic_scenarios"),
    )
    op.create_index("ix_strategic_scenarios_organization_id", "strategic_scenarios", ["organization_id"])
    op.create_index("ix_strategic_scenarios_risk_origin_id", "strategic_scenarios", ["risk_origin_id"])
    op.create_index("ix_strategic_scenarios_feared_event_id", "strategic_scenarios", ["feared_event_id"])
    op.create_index("ix_strategic_scenarios_ecosystem_party_id", "strategic_scenarios", ["ecosystem_party_id"])


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
    _create_ecosystem_parties_table()
    _create_strategic_scenarios_table()
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

    op.drop_index("ix_strategic_scenarios_ecosystem_party_id", table_name="strategic_scenarios")
    op.drop_index("ix_strategic_scenarios_feared_event_id", table_name="strategic_scenarios")
    op.drop_index("ix_strategic_scenarios_risk_origin_id", table_name="strategic_scenarios")
    op.drop_index("ix_strategic_scenarios_organization_id", table_name="strategic_scenarios")
    op.drop_table("strategic_scenarios")
    postgresql.ENUM(name="strategicscenariolikelihood").drop(op.get_bind(), checkfirst=True)

    op.drop_index("ix_ecosystem_parties_organization_id", table_name="ecosystem_parties")
    op.drop_table("ecosystem_parties")
    for name in ("ecosystempartylevel", "ecosystempartycategory"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
