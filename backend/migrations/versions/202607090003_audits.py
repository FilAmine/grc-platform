"""audits: planning, checklists, findings, corrective actions

Revision ID: 202607090003
Revises: 202607090002
Create Date: 2026-07-09 00:03:00
"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "202607090003"
down_revision: str | None = "202607090002"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # create_type=False: see 202606250001_initial_schema.py for why.
    auditstatus = postgresql.ENUM(
        "PLANNED", "IN_PROGRESS", "COMPLETED", "CLOSED", name="auditstatus", create_type=False
    )
    checkliststatus = postgresql.ENUM(
        "PENDING", "DONE", "NOT_APPLICABLE", name="checklistitemstatus", create_type=False
    )
    findingseverity = postgresql.ENUM(
        "MINOR", "MAJOR", "CRITICAL", name="findingseverity", create_type=False
    )
    findingstatus = postgresql.ENUM(
        "OPEN", "IN_REMEDIATION", "CLOSED", name="findingstatus", create_type=False
    )
    correctiveactionstatus = postgresql.ENUM(
        "OPEN", "IN_PROGRESS", "DONE", name="correctiveactionstatus", create_type=False
    )
    for enum in (auditstatus, checkliststatus, findingseverity, findingstatus, correctiveactionstatus):
        enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "audits",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("scope", sa.Text(), nullable=False),
        sa.Column("lead_auditor", sa.String(length=255), nullable=False),
        sa.Column("status", auditstatus, nullable=False),
        sa.Column("period_start", sa.Date(), nullable=True),
        sa.Column("period_end", sa.Date(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_audits_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="fk_audits_created_by_id_users", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["updated_by_id"], ["users.id"], name="fk_audits_updated_by_id_users", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_audits"),
    )
    op.create_index("ix_audits_organization_id", "audits", ["organization_id"])

    op.create_table(
        "checklist_items",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("audit_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("status", checkliststatus, nullable=False),
        sa.Column("notes", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["audit_id"], ["audits.id"], name="fk_checklist_items_audit_id_audits", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_checklist_items"),
    )
    op.create_index("ix_checklist_items_audit_id", "checklist_items", ["audit_id"])

    op.create_table(
        "findings",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("audit_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("checklist_item_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("severity", findingseverity, nullable=False),
        sa.Column("status", findingstatus, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["audit_id"], ["audits.id"], name="fk_findings_audit_id_audits", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["checklist_item_id"], ["checklist_items.id"], name="fk_findings_checklist_item_id_checklist_items", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_findings"),
    )
    op.create_index("ix_findings_audit_id", "findings", ["audit_id"])

    op.create_table(
        "corrective_actions",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("finding_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("owner", sa.String(length=255), nullable=False),
        sa.Column("due_date", sa.Date(), nullable=True),
        sa.Column("status", correctiveactionstatus, nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["finding_id"], ["findings.id"], name="fk_corrective_actions_finding_id_findings", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_corrective_actions"),
    )
    op.create_index("ix_corrective_actions_finding_id", "corrective_actions", ["finding_id"])


def downgrade() -> None:
    op.drop_index("ix_corrective_actions_finding_id", table_name="corrective_actions")
    op.drop_table("corrective_actions")
    op.drop_index("ix_findings_audit_id", table_name="findings")
    op.drop_table("findings")
    op.drop_index("ix_checklist_items_audit_id", table_name="checklist_items")
    op.drop_table("checklist_items")
    op.drop_index("ix_audits_organization_id", table_name="audits")
    op.drop_table("audits")
    for name in ("correctiveactionstatus", "findingstatus", "findingseverity", "checklistitemstatus", "auditstatus"):
        postgresql.ENUM(name=name).drop(op.get_bind(), checkfirst=True)
