"""sso_connections (per-organization OIDC configuration)

Revision ID: 202607100003
Revises: 202607100002
Create Date: 2026-07-10 00:03:00

One row per organization (enforced by the unique constraint on
organization_id). client_secret is stored in plaintext -- no
KMS/envelope-encryption infra exists in this codebase; see docs/security.md's
SSO section for this known limitation.
"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "202607100003"
down_revision: str | None = "202607100002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "sso_connections",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("issuer", sa.String(length=500), nullable=False),
        sa.Column("client_id", sa.String(length=255), nullable=False),
        sa.Column("client_secret", sa.String(length=500), nullable=False),
        sa.Column("default_role_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("is_enabled", sa.Boolean(), nullable=False),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"], ["organizations.id"],
            name="fk_sso_connections_organization_id_organizations", ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["default_role_id"], ["roles.id"], name="fk_sso_connections_default_role_id_roles", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["created_by_id"], ["users.id"], name="fk_sso_connections_created_by_id_users", ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"], ["users.id"], name="fk_sso_connections_updated_by_id_users", ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", name="pk_sso_connections"),
        # Unique constraint doubles as the lookup index for get_by_organization
        # (one row per org) -- no separate ix_ needed, Postgres backs UNIQUE
        # constraints with an index automatically.
        sa.UniqueConstraint("organization_id", name="uq_sso_connections_organization_id"),
    )


def downgrade() -> None:
    op.drop_table("sso_connections")
