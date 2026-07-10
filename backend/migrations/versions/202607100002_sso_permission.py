"""add sso:manage permission and backfill it onto the Admin system role

Revision ID: 202607100002
Revises: 202607100001
Create Date: 2026-07-10 00:02:00

This is the first real instance of the gotcha `202607090001` warned about:
"any permission codes added to security/permissions.py after [that migration]
has actually been applied to a database need their own follow-up migration to
insert the delta." `Admin`'s "all permissions" is a snapshot resolved *once*
at seed time (see security/permissions.py's SYSTEM_ROLES comment), not a
dynamic "all permissions that currently exist" check -- so a brand-new
permission does not automatically reach the already-seeded global `Admin`
role. This migration ensures the `sso:manage` permission row exists and is
granted to the single global `Admin` system role (`organization_id IS NULL`,
looked up by name -- there is exactly one, per the existing system-role
pattern).

Both the insert and the grant are idempotent (find-or-create), not blind
inserts: on a database that has *never* been migrated before this code
existed, `202607090001`'s dynamic seed step (it imports ALL_PERMISSIONS at
migration *run time*) already picks up `sso:manage` and grants it to `Admin`
as part of the initial seed, since the permission is already in
security/permissions.py by then. A blind `INSERT` here would hit a duplicate
key error in that case -- confirmed against a real local Postgres instance,
not just reasoned about.

Like `202607100001`, this migration runs a runtime SELECT (to find the
existing Admin role's id), so it has no meaningful `--sql` offline preview --
upgrade()/downgrade() are no-ops in offline mode; a real `alembic upgrade
head` against a live database runs normally.
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607100002"
down_revision: str | None = "202607100001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSION_CODE = "sso:manage"
PERMISSION_DESCRIPTION = "Configure the organization's SSO (OIDC) connection"


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


def upgrade() -> None:
    if context.is_offline_mode():
        return
    bind = op.get_bind()
    permissions = _permissions_table()
    role_permissions = _role_permissions_table()
    roles = _roles_table()

    permission_id = bind.execute(
        sa.select(permissions.c.id).where(permissions.c.code == PERMISSION_CODE)
    ).scalar_one_or_none()
    if permission_id is None:
        now = datetime.now(UTC)
        permission_id = uuid4()
        op.bulk_insert(
            permissions,
            [
                {
                    "id": permission_id,
                    "code": PERMISSION_CODE,
                    "description": PERMISSION_DESCRIPTION,
                    "created_at": now,
                    "updated_at": now,
                }
            ],
        )

    admin_role_id = bind.execute(
        sa.select(roles.c.id).where(
            sa.and_(roles.c.name == "Admin", roles.c.organization_id.is_(None), roles.c.is_system.is_(True))
        )
    ).scalar_one_or_none()
    if admin_role_id is None:
        return

    already_granted = bind.execute(
        sa.select(role_permissions.c.role_id).where(
            sa.and_(
                role_permissions.c.role_id == admin_role_id,
                role_permissions.c.permission_id == permission_id,
            )
        )
    ).scalar_one_or_none()
    if already_granted is None:
        op.bulk_insert(
            role_permissions,
            [{"role_id": admin_role_id, "permission_id": permission_id}],
        )


def downgrade() -> None:
    if context.is_offline_mode():
        return
    bind = op.get_bind()
    permissions = _permissions_table()
    role_permissions = _role_permissions_table()

    permission_id = bind.execute(
        sa.select(permissions.c.id).where(permissions.c.code == PERMISSION_CODE)
    ).scalar_one_or_none()
    if permission_id is not None:
        op.execute(role_permissions.delete().where(role_permissions.c.permission_id == permission_id))
        op.execute(permissions.delete().where(permissions.c.id == permission_id))
