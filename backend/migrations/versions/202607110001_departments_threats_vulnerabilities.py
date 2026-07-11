"""departments, threats, vulnerabilities

Revision ID: 202607110001
Revises: 202607100003
Create Date: 2026-07-11 00:01:00

Adds three standalone catalog/register tables named separately in the spec's
module list but missing from this build: a department hierarchy under an
organization, a threat catalog, and a vulnerability register. None of the
three are cross-linked to risks/assets yet -- that wiring belongs to the
separate, larger EBIOS RM item tracked in docs/roadmap.md.

Like `202607100002`, this migration also has to backfill the 6 new
permission codes onto the pre-existing global system roles (Admin, Manager,
Auditor, Viewer) idempotently: those roles are singletons
(`organization_id IS NULL`) seeded once by `202607090001`, and Admin's "all
permissions" is a one-time snapshot resolved at that seed time, not a
dynamic "all permissions that currently exist" check -- so an
already-migrated database's Admin role does not automatically pick up
brand-new codes. A fresh `alembic upgrade head` on a new database picks
these up automatically via `202607090001`'s dynamic seed step (it imports
`security.permissions.ALL_PERMISSIONS`/`SYSTEM_ROLES` at migration run
time), which is exactly why the permission/role-grant inserts below are
find-or-create, not blind inserts -- see `202607100002`'s docstring for the
duplicate-key trap this avoids.
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607110001"
down_revision: str | None = "202607100003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

# code -> description, matching security/permissions.py
PERMISSIONS: dict[str, str] = {
    "departments:read": "View the department hierarchy",
    "departments:manage": "Create departments",
    "threats:read": "View the threat catalog",
    "threats:manage": "Create threats",
    "vulnerabilities:read": "View the vulnerability register",
    "vulnerabilities:manage": "Create vulnerabilities",
}

# role name -> permission codes granted, matching security/permissions.py's
# SYSTEM_ROLES for these 6 codes specifically.
ROLE_GRANTS: dict[str, tuple[str, ...]] = {
    "Admin": tuple(PERMISSIONS.keys()),
    "Manager": tuple(PERMISSIONS.keys()),
    "Auditor": ("departments:read", "threats:read", "vulnerabilities:read"),
    "Viewer": ("departments:read", "threats:read", "vulnerabilities:read"),
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


def _create_tables() -> None:
    threatcategory = postgresql.ENUM(
        "HUMAN", "TECHNICAL", "ENVIRONMENTAL", "ORGANIZATIONAL", name="threatcategory", create_type=False
    )
    threatlikelihood = postgresql.ENUM("LOW", "MEDIUM", "HIGH", name="threatlikelihood", create_type=False)
    vulnerabilityseverity = postgresql.ENUM(
        "LOW", "MEDIUM", "HIGH", "CRITICAL", name="vulnerabilityseverity", create_type=False
    )
    vulnerabilitystatus = postgresql.ENUM(
        "OPEN", "MITIGATED", "ACCEPTED", "CLOSED", name="vulnerabilitystatus", create_type=False
    )
    for enum in (threatcategory, threatlikelihood, vulnerabilityseverity, vulnerabilitystatus):
        enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "departments",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("parent_department_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_departments_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["parent_department_id"], ["departments.id"], name="fk_departments_parent_department_id_departments",
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_departments_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_departments_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_departments"),
    )
    op.create_index("ix_departments_organization_id", "departments", ["organization_id"])
    op.create_index("ix_departments_parent_department_id", "departments", ["parent_department_id"])

    op.create_table(
        "threats",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("category", threatcategory, nullable=False),
        sa.Column("likelihood", threatlikelihood, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_threats_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_threats_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_threats_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_threats"),
    )
    op.create_index("ix_threats_organization_id", "threats", ["organization_id"])

    op.create_table(
        "vulnerabilities",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("severity", vulnerabilityseverity, nullable=False),
        sa.Column("status", vulnerabilitystatus, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_vulnerabilities_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_vulnerabilities_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_vulnerabilities_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_vulnerabilities"),
    )
    op.create_index("ix_vulnerabilities_organization_id", "vulnerabilities", ["organization_id"])


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
    _create_tables()
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

    op.drop_index("ix_vulnerabilities_organization_id", table_name="vulnerabilities")
    op.drop_table("vulnerabilities")
    op.drop_index("ix_threats_organization_id", table_name="threats")
    op.drop_table("threats")
    op.drop_index("ix_departments_parent_department_id", table_name="departments")
    op.drop_index("ix_departments_organization_id", table_name="departments")
    op.drop_table("departments")
    for name in ("vulnerabilitystatus", "vulnerabilityseverity", "threatlikelihood", "threatcategory"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
