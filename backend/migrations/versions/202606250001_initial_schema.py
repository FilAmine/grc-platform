"""initial schema

Revision ID: 202606250001
Revises:
Create Date: 2026-06-25 00:01:00
"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "202606250001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    riskseverity = postgresql.ENUM("LOW", "MEDIUM", "HIGH", "CRITICAL", name="riskseverity")
    riskstatus = postgresql.ENUM("OPEN", "MITIGATING", "ACCEPTED", "CLOSED", name="riskstatus")
    controlstatus = postgresql.ENUM("DRAFT", "ACTIVE", "RETIRED", name="controlstatus")
    riskseverity.create(op.get_bind(), checkfirst=True)
    riskstatus.create(op.get_bind(), checkfirst=True)
    controlstatus.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "organizations",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=100), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_organizations_slug"), "organizations", ["slug"], unique=True)

    op.create_table(
        "controls",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("framework", sa.String(length=100), nullable=False),
        sa.Column("status", controlstatus, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_controls_organization_id"), "controls", ["organization_id"], unique=False)

    op.create_table(
        "risks",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("severity", riskseverity, nullable=False),
        sa.Column("status", riskstatus, nullable=False),
        sa.Column("owner", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_risks_organization_id"), "risks", ["organization_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_risks_organization_id"), table_name="risks")
    op.drop_table("risks")
    op.drop_index(op.f("ix_controls_organization_id"), table_name="controls")
    op.drop_table("controls")
    op.drop_index(op.f("ix_organizations_slug"), table_name="organizations")
    op.drop_table("organizations")
    postgresql.ENUM(name="controlstatus").drop(op.get_bind(), checkfirst=True)
    postgresql.ENUM(name="riskstatus").drop(op.get_bind(), checkfirst=True)
    postgresql.ENUM(name="riskseverity").drop(op.get_bind(), checkfirst=True)
