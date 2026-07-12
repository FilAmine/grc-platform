"""tenants + generic tasks

Revision ID: 202607140001
Revises: 202607130001
Create Date: 2026-07-14 00:01:00

Adds a `Tenant` entity ABOVE `Organization` (a nullable `tenant_id` FK on the
pre-existing `organizations` table) and a standalone `Task` module. This
closes the "tenants-as-distinct-from-organizations, generic
tasks-as-a-module" roadmap gap -- previously a resolved decision in
docs/roadmap.md ("this build treats organizations as the tenant root, no
separate tenants entity"), now reversed.

`tenants` does NOT carry `organization_id` -- it isn't tenant-scoped, it's
the reverse direction: organizations optionally belong to a tenant. The
actual tenant-ISOLATION boundary (`organization_id`, enforced by every
`TenantScopedMixin` table) is completely unaffected by this migration. See
`backend/app/modules/tenants/models.py`'s docstring for the full
terminology disambiguation ("tenant" now means two different things in this
codebase, stated plainly rather than hidden).

`tenants` must be created before `organizations.tenant_id`'s FK constraint
is added (same ordering constraint `202607130001` established for
`feared_events`/`risks`). This is the second migration in this repo to
`ALTER` a pre-existing table.

`tasks` follows the standard tenant-scoped catalog shape (matches
`incidents`); its `status` column is driven by a real `StateMachine`
(`start`/`complete`/`reopen`, no direct `OPEN<->DONE` jump) rather than a
plain settable enum, since it's a standalone module with its own top-level
status endpoint -- matching `audits`/`incidents`, not the plain-status
audit-child tables (`checklist_items`/`findings`/`corrective_actions`),
which are only reachable through an already-ownership-checked parent and
have no `organization_id` of their own.

Also seeds `tasks:read`/`tasks:manage` following the idempotent
find-or-create pattern from `202607120001`/`202607130001` -- no permission
codes are added for `Tenant` at all (see `tenants/api.py`: gated by a raw
`is_superuser` check, same as `organizations/api.py`, deliberately not
`require_permission`, since that would make a platform-level, cross-org
capability delegable to a per-org role).
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import context, op
from sqlalchemy.dialects import postgresql

revision: str = "202607140001"
down_revision: str | None = "202607130001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSIONS: dict[str, str] = {
    "tasks:read": "View tasks",
    "tasks:manage": "Create tasks and change their status",
}

ROLE_GRANTS: dict[str, tuple[str, ...]] = {
    "Admin": tuple(PERMISSIONS.keys()),
    "Manager": tuple(PERMISSIONS.keys()),
    "Auditor": ("tasks:read",),
    "Viewer": ("tasks:read",),
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


def _create_tenants_table() -> None:
    op.create_table(
        "tenants",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_tenants_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_tenants_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_tenants"),
    )
    op.create_index("ix_tenants_slug", "tenants", ["slug"], unique=True)


def _add_organization_tenant_column() -> None:
    op.add_column("organizations", sa.Column("tenant_id", postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(
        "fk_organizations_tenant_id_tenants",
        "organizations", "tenants", ["tenant_id"], ["id"], ondelete="SET NULL",
    )
    op.create_index("ix_organizations_tenant_id", "organizations", ["tenant_id"])


def _create_tasks_table() -> None:
    taskstatus = postgresql.ENUM("OPEN", "IN_PROGRESS", "DONE", name="taskstatus", create_type=False)
    taskstatus.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "tasks",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("status", taskstatus, nullable=False),
        sa.Column("due_date", sa.Date(), nullable=True),
        sa.Column("assignee", sa.String(length=255), nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_tasks_organization_id_organizations",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_tasks_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_tasks_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_tasks"),
    )
    op.create_index("ix_tasks_organization_id", "tasks", ["organization_id"])


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
    _create_tenants_table()
    _add_organization_tenant_column()
    _create_tasks_table()
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

    op.drop_index("ix_tasks_organization_id", table_name="tasks")
    op.drop_table("tasks")
    postgresql.ENUM(name="taskstatus").drop(op.get_bind(), checkfirst=True)

    op.drop_index("ix_organizations_tenant_id", table_name="organizations")
    op.drop_constraint("fk_organizations_tenant_id_tenants", "organizations", type_="foreignkey")
    op.drop_column("organizations", "tenant_id")

    op.drop_index("ix_tenants_slug", table_name="tenants")
    op.drop_table("tenants")
