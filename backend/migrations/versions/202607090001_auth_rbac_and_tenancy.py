"""auth, RBAC, and tenancy retrofit

Revision ID: 202607090001
Revises: 202606250001
Create Date: 2026-07-09 00:01:00

Note on the permission seed at the bottom of upgrade(): it imports
ALL_PERMISSIONS/SYSTEM_ROLES from backend.app.security.permissions at
migration *run* time, not at the time this file was written, so a fresh
`alembic upgrade head` always seeds whatever permission codes exist in that
module today. But once this migration has actually been applied to a
database, it will not run again -- any permission codes added to
security/permissions.py *after* that point need their own follow-up
migration to insert the delta (see how later modules such as compliance/
audits/ai added permission codes without re-seeding here).
"""
from collections.abc import Sequence
from datetime import UTC, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import op
from backend.app.security.permissions import ALL_PERMISSIONS, SYSTEM_ROLES
from sqlalchemy.dialects import postgresql

revision: str = "202607090001"
down_revision: str | None = "202606250001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # --- retrofit tenant/soft-delete/audit columns on pre-existing tables ---
    # created_by_id/updated_by_id -> users.id constraints are added later, once
    # the users table exists, to break the organizations<->users circular reference.
    op.add_column("organizations", sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True))
    op.add_column("organizations", sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True))
    op.add_column("organizations", sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True))

    for table in ("risks", "controls"):
        op.add_column(table, sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True))
        op.add_column(table, sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True))
        op.add_column(table, sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True))

    # --- users ---
    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("failed_login_attempts", sa.Integer(), nullable=False),
        sa.Column("locked_until", sa.DateTime(timezone=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_users_organization_id_organizations", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_users"),
    )
    op.create_index("ix_users_organization_id", "users", ["organization_id"])
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    # --- circular FKs now resolvable ---
    op.create_foreign_key(
        "fk_organizations_created_by_id_users", "organizations", "users", ["created_by_id"], ["id"], ondelete="SET NULL"
    )
    op.create_foreign_key(
        "fk_organizations_updated_by_id_users", "organizations", "users", ["updated_by_id"], ["id"], ondelete="SET NULL"
    )
    for table in ("risks", "controls"):
        op.create_foreign_key(
            f"fk_{table}_created_by_id_users", table, "users", ["created_by_id"], ["id"], ondelete="SET NULL"
        )
        op.create_foreign_key(
            f"fk_{table}_updated_by_id_users", table, "users", ["updated_by_id"], ["id"], ondelete="SET NULL"
        )

    # --- permissions catalog ---
    op.create_table(
        "permissions",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("code", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name="pk_permissions"),
    )
    op.create_index("ix_permissions_code", "permissions", ["code"], unique=True)

    # --- roles ---
    op.create_table(
        "roles",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column("is_system", sa.Boolean(), nullable=False),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"], name="fk_roles_organization_id_organizations", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_roles_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_roles_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_roles"),
    )
    op.create_index("ix_roles_organization_id", "roles", ["organization_id"])

    # --- role_permissions, user_roles (association tables) ---
    op.create_table(
        "role_permissions",
        sa.Column("role_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("permission_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(["role_id"], ["roles.id"], name="fk_role_permissions_role_id_roles", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["permission_id"], ["permissions.id"], name="fk_role_permissions_permission_id_permissions", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("role_id", "permission_id", name="pk_role_permissions"),
    )
    op.create_table(
        "user_roles",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_roles_user_id_users", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["role_id"], ["roles.id"], name="fk_user_roles_role_id_roles", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "role_id", name="pk_user_roles"),
    )

    # --- refresh tokens ---
    op.create_table(
        "refresh_tokens",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("token_hash", sa.String(length=64), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("revoked_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_refresh_tokens_user_id_users", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_refresh_tokens"),
    )
    op.create_index("ix_refresh_tokens_user_id", "refresh_tokens", ["user_id"])
    op.create_index("ix_refresh_tokens_token_hash", "refresh_tokens", ["token_hash"], unique=True)

    # --- seed the permission catalog and default system roles ---
    permissions_table = sa.table(
        "permissions",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
        sa.column("description", sa.String),
        sa.column("created_at", sa.DateTime(timezone=True)),
        sa.column("updated_at", sa.DateTime(timezone=True)),
    )
    roles_table = sa.table(
        "roles",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("organization_id", postgresql.UUID(as_uuid=True)),
        sa.column("name", sa.String),
        sa.column("description", sa.String),
        sa.column("is_system", sa.Boolean),
        sa.column("created_at", sa.DateTime(timezone=True)),
        sa.column("updated_at", sa.DateTime(timezone=True)),
    )
    role_permissions_table = sa.table(
        "role_permissions",
        sa.column("role_id", postgresql.UUID(as_uuid=True)),
        sa.column("permission_id", postgresql.UUID(as_uuid=True)),
    )

    now = datetime.now(UTC)
    permission_ids: dict[str, object] = {}
    permission_rows = []
    for perm in ALL_PERMISSIONS:
        perm_id = uuid4()
        permission_ids[perm.code] = perm_id
        permission_rows.append(
            {"id": perm_id, "code": perm.code, "description": perm.description, "created_at": now, "updated_at": now}
        )
    op.bulk_insert(permissions_table, permission_rows)

    role_rows = []
    role_permission_rows = []
    for role_name, codes in SYSTEM_ROLES.items():
        role_id = uuid4()
        role_rows.append(
            {
                "id": role_id,
                "organization_id": None,
                "name": role_name,
                "description": f"System role: {role_name}",
                "is_system": True,
                "created_at": now,
                "updated_at": now,
            }
        )
        granted_codes = list(permission_ids.keys()) if codes is None else list(codes)
        for code in granted_codes:
            role_permission_rows.append({"role_id": role_id, "permission_id": permission_ids[code]})
    op.bulk_insert(roles_table, role_rows)
    op.bulk_insert(role_permissions_table, role_permission_rows)


def downgrade() -> None:
    op.drop_index("ix_refresh_tokens_token_hash", table_name="refresh_tokens")
    op.drop_index("ix_refresh_tokens_user_id", table_name="refresh_tokens")
    op.drop_table("refresh_tokens")
    op.drop_table("user_roles")
    op.drop_table("role_permissions")
    op.drop_index("ix_roles_organization_id", table_name="roles")
    op.drop_table("roles")
    op.drop_index("ix_permissions_code", table_name="permissions")
    op.drop_table("permissions")

    for table in ("risks", "controls"):
        op.drop_constraint(f"fk_{table}_updated_by_id_users", table, type_="foreignkey")
        op.drop_constraint(f"fk_{table}_created_by_id_users", table, type_="foreignkey")
    op.drop_constraint("fk_organizations_updated_by_id_users", "organizations", type_="foreignkey")
    op.drop_constraint("fk_organizations_created_by_id_users", "organizations", type_="foreignkey")

    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_organization_id", table_name="users")
    op.drop_table("users")

    for table in ("risks", "controls"):
        op.drop_column(table, "updated_by_id")
        op.drop_column(table, "created_by_id")
        op.drop_column(table, "deleted_at")
    op.drop_column("organizations", "updated_by_id")
    op.drop_column("organizations", "created_by_id")
    op.drop_column("organizations", "deleted_at")
