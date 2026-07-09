"""documents: policies, versioning, approval workflow

Revision ID: 202607090004
Revises: 202607090003
Create Date: 2026-07-09 00:04:00
"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "202607090004"
down_revision: str | None = "202607090003"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    documenttype = postgresql.ENUM("POLICY", "PROCEDURE", "STANDARD", "GUIDELINE", "TEMPLATE", name="documenttype")
    documentstatus = postgresql.ENUM("DRAFT", "IN_REVIEW", "PUBLISHED", "ARCHIVED", name="documentstatus")
    versionstatus = postgresql.ENUM("DRAFT", "PENDING_APPROVAL", "APPROVED", "REJECTED", name="versionstatus")
    for enum in (documenttype, documentstatus, versionstatus):
        enum.create(op.get_bind(), checkfirst=True)

    # documents.published_version_id references document_versions, which references
    # documents -- created without that FK first, added via ALTER once both tables exist.
    op.create_table(
        "documents",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("document_type", documenttype, nullable=False),
        sa.Column("status", documentstatus, nullable=False),
        sa.Column("owner", sa.String(length=255), nullable=False),
        sa.Column("published_version_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_documents_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="fk_documents_created_by_id_users", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["updated_by_id"], ["users.id"], name="fk_documents_updated_by_id_users", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_documents"),
    )
    op.create_index("ix_documents_organization_id", "documents", ["organization_id"])

    op.create_table(
        "document_versions",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("document_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("version_number", sa.Integer(), nullable=False),
        sa.Column("file_reference", sa.String(length=1024), nullable=False),
        sa.Column("change_summary", sa.Text(), nullable=False),
        sa.Column("status", versionstatus, nullable=False),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], name="fk_document_versions_document_id_documents", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="fk_document_versions_created_by_id_users", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_document_versions"),
    )
    op.create_index("ix_document_versions_document_id", "document_versions", ["document_id"])

    op.create_foreign_key(
        "fk_documents_published_version_id_document_versions",
        "documents", "document_versions", ["published_version_id"], ["id"], ondelete="SET NULL",
    )

    op.create_table(
        "document_approvals",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("document_version_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("approver_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("decision", versionstatus, nullable=False),
        sa.Column("comment", sa.Text(), nullable=False),
        sa.Column("signature_reference", sa.String(length=255), nullable=True),
        sa.Column("decided_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["document_version_id"], ["document_versions.id"], name="fk_document_approvals_document_version_id_document_versions", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["approver_id"], ["users.id"], name="fk_document_approvals_approver_id_users", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_document_approvals"),
    )
    op.create_index("ix_document_approvals_document_version_id", "document_approvals", ["document_version_id"])


def downgrade() -> None:
    op.drop_index("ix_document_approvals_document_version_id", table_name="document_approvals")
    op.drop_table("document_approvals")
    op.drop_constraint("fk_documents_published_version_id_document_versions", "documents", type_="foreignkey")
    op.drop_index("ix_document_versions_document_id", table_name="document_versions")
    op.drop_table("document_versions")
    op.drop_index("ix_documents_organization_id", table_name="documents")
    op.drop_table("documents")
    for name in ("versionstatus", "documentstatus", "documenttype"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
