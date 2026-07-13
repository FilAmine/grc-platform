"""EBIOS RM Workshop 5: risk treatment

Revision ID: 202607180001
Revises: 202607170001
Create Date: 2026-07-18 00:01:00

The final workshop of the 5-workshop ANSSI methodology. Synthesizes a
Workshop 3 strategic scenario (optionally detailed further by Workshop 4
operational scenarios, though this table links directly to the strategic
scenario, not the operational one -- a treatment decision can be made
before a scenario has been technically detailed) into a treatment
decision: avoid, reduce, transfer, or accept (the standard ISO 27005 /
EBIOS RM 4-way choice), plus the residual risk level left over after
applying it.

One new table, `risk_treatments`. `strategic_scenario_id` is mandatory
(`ondelete="RESTRICT"`) -- a risk treatment *is* a decision about a
specific strategic scenario, same reasoning every other EBIOS RM FK chain
this session has used. Deliberately no uniqueness constraint on
`strategic_scenario_id`: a scenario can have more than one treatment
record over time (re-deciding means creating a new row, an append-only
decision history, not mutating one in place -- matching the list+create-only,
no-update-endpoint shape every EBIOS RM module this session has used).

Follows the idempotent permission-seeding pattern established by
202607120001 onward for the 2 new `risk_treatments:*` codes.
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607180001"
down_revision: str | None = "202607170001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSIONS: dict[str, str] = {
    "risk_treatments:read": "View EBIOS RM risk treatment decisions",
    "risk_treatments:manage": "Record risk treatment decisions",
}

ROLE_GRANTS: dict[str, tuple[str, ...]] = {
    "Admin": tuple(PERMISSIONS.keys()),
    "Manager": tuple(PERMISSIONS.keys()),
    "Auditor": ("risk_treatments:read",),
    "Viewer": ("risk_treatments:read",),
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


def _create_risk_treatments_table() -> None:
    decision = postgresql.ENUM(
        "AVOID", "REDUCE", "TRANSFER", "ACCEPT", name="risktreatmentdecision", create_type=False
    )
    residual_risk = postgresql.ENUM(
        "LOW", "MEDIUM", "HIGH", "CRITICAL", name="risktreatmentresidualrisk", create_type=False
    )
    for enum in (decision, residual_risk):
        enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "risk_treatments",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("strategic_scenario_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("decision", decision, nullable=False),
        sa.Column("justification", sa.Text(), nullable=False),
        sa.Column("residual_risk_level", residual_risk, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"],
            name="fk_risk_treatments_organization_id_organizations", ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["strategic_scenario_id"], ["strategic_scenarios.id"],
            name="fk_risk_treatments_strategic_scenario_id_strategic_scenarios", ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_risk_treatments_created_by_id_users",
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_risk_treatments_updated_by_id_users",
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_risk_treatments"),
    )
    op.create_index("ix_risk_treatments_organization_id", "risk_treatments", ["organization_id"])
    op.create_index("ix_risk_treatments_strategic_scenario_id", "risk_treatments", ["strategic_scenario_id"])


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
    _create_risk_treatments_table()
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

    op.drop_index("ix_risk_treatments_strategic_scenario_id", table_name="risk_treatments")
    op.drop_index("ix_risk_treatments_organization_id", table_name="risk_treatments")
    op.drop_table("risk_treatments")
    for name in ("risktreatmentresidualrisk", "risktreatmentdecision"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
