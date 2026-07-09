"""notifications

Revision ID: 202607090007
Revises: 202607090006
Create Date: 2026-07-09 00:07:00
"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "202607090007"
down_revision: str | None = "202607090006"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "notifications",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("recipient_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("subject", sa.String(length=255), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("read_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_notifications_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["recipient_id"], ["users.id"], name="fk_notifications_recipient_id_users", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_notifications"),
    )
    op.create_index("ix_notifications_organization_id", "notifications", ["organization_id"])
    op.create_index("ix_notifications_recipient_id", "notifications", ["recipient_id"])


def downgrade() -> None:
    op.drop_index("ix_notifications_recipient_id", table_name="notifications")
    op.drop_index("ix_notifications_organization_id", table_name="notifications")
    op.drop_table("notifications")
