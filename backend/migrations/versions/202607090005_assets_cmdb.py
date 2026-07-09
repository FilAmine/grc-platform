"""assets / CMDB

Revision ID: 202607090005
Revises: 202607090004
Create Date: 2026-07-09 00:05:00
"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "202607090005"
down_revision: str | None = "202607090004"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # create_type=False: see 202606250001_initial_schema.py for why.
    assettype = postgresql.ENUM(
        "HARDWARE", "SOFTWARE", "CLOUD_SERVICE", "APPLICATION", "BUSINESS_ASSET", "SERVICE",
        name="assettype", create_type=False,
    )
    lifecycle = postgresql.ENUM(
        "PLANNED", "IN_USE", "MAINTENANCE", "RETIRED", "DISPOSED", name="assetlifecyclestage", create_type=False
    )
    classification = postgresql.ENUM("LOW", "MEDIUM", "HIGH", name="classificationlevel", create_type=False)
    for enum in (assettype, lifecycle, classification):
        enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "assets",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("asset_type", assettype, nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("owner", sa.String(length=255), nullable=False),
        sa.Column("supplier", sa.String(length=255), nullable=False),
        sa.Column("lifecycle_stage", lifecycle, nullable=False),
        sa.Column("confidentiality", classification, nullable=False),
        sa.Column("integrity", classification, nullable=False),
        sa.Column("availability", classification, nullable=False),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_assets_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="fk_assets_created_by_id_users", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["updated_by_id"], ["users.id"], name="fk_assets_updated_by_id_users", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_assets"),
    )
    op.create_index("ix_assets_organization_id", "assets", ["organization_id"])


def downgrade() -> None:
    op.drop_index("ix_assets_organization_id", table_name="assets")
    op.drop_table("assets")
    for name in ("classificationlevel", "assetlifecyclestage", "assettype"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
