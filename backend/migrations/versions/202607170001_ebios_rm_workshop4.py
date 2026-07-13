"""EBIOS RM Workshop 4: operational scenarios

Revision ID: 202607170001
Revises: 202607160001
Create Date: 2026-07-17 00:01:00

Workshop 3 (202607160001) added ecosystem mapping and strategic scenarios
(the "what and why" of an attack path). This migration adds Workshop 4:
operational scenarios, which elaborate a strategic scenario into a
concrete technical attack chain (the "how").

One new table, `operational_scenarios`:

- `strategic_scenario_id` is mandatory (`ondelete="RESTRICT"`) -- an
  operational scenario *is* the technical elaboration of a specific
  strategic scenario, same reasoning `202607160001` used for
  `strategic_scenarios.risk_origin_id`/`feared_event_id`.
- `mitre_technique_ids` is a plain JSON column (not a Postgres-specific
  ARRAY), storing a free-text list of technique identifiers -- runs against
  any SQL backend (SQLite in tests, Postgres in prod), same reasoning
  `KnowledgeBaseDocumentModel.embedding` already established for this
  codebase. Not validated against a live MITRE ATT&CK catalog; see
  `backend/app/modules/operational_scenarios/service.py`'s docstring for
  why that's out of scope.
- `technical_likelihood` is a separate field from the linked strategic
  scenario's own `likelihood` -- one captures attacker motivation/
  targeting, the other technical feasibility; the two can diverge.

Follows the idempotent permission-seeding pattern established by
202607120001 onward for the 2 new `operational_scenarios:*` codes.
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607170001"
down_revision: str | None = "202607160001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSIONS: dict[str, str] = {
    "operational_scenarios:read": "View EBIOS RM operational scenarios",
    "operational_scenarios:manage": "Create operational scenarios",
}

ROLE_GRANTS: dict[str, tuple[str, ...]] = {
    "Admin": tuple(PERMISSIONS.keys()),
    "Manager": tuple(PERMISSIONS.keys()),
    "Auditor": ("operational_scenarios:read",),
    "Viewer": ("operational_scenarios:read",),
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


def _create_operational_scenarios_table() -> None:
    likelihood = postgresql.ENUM(
        "LOW", "MEDIUM", "HIGH", "CRITICAL", name="operationalscenariolikelihood", create_type=False
    )
    likelihood.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "operational_scenarios",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("strategic_scenario_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("mitre_technique_ids", sa.JSON(), nullable=False),
        sa.Column("technical_likelihood", likelihood, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"],
            name="fk_operational_scenarios_organization_id_organizations", ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["strategic_scenario_id"], ["strategic_scenarios.id"],
            name="fk_operational_scenarios_strategic_scenario_id_strategic_scenarios", ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_operational_scenarios_created_by_id_users",
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_operational_scenarios_updated_by_id_users",
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_operational_scenarios"),
    )
    op.create_index("ix_operational_scenarios_organization_id", "operational_scenarios", ["organization_id"])
    op.create_index(
        "ix_operational_scenarios_strategic_scenario_id", "operational_scenarios", ["strategic_scenario_id"]
    )


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
    _create_operational_scenarios_table()
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

    op.drop_index("ix_operational_scenarios_strategic_scenario_id", table_name="operational_scenarios")
    op.drop_index("ix_operational_scenarios_organization_id", table_name="operational_scenarios")
    op.drop_table("operational_scenarios")
    postgresql.ENUM(name="operationalscenariolikelihood").drop(op.get_bind(), checkfirst=True)
