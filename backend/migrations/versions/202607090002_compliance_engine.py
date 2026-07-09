"""generic compliance engine: frameworks, requirements, assessments, evidence

Revision ID: 202607090002
Revises: 202607090001
Create Date: 2026-07-09 00:02:00

Seeds the framework *catalog* (name/code/version) for the standards named in
the product spec (ISO 27001/27002/27005, NIST CSF, NIS2, DORA, CIS Controls,
SOC 2, PCI DSS, HIPAA) plus a small, illustrative set of real ISO 27001:2022
Annex A requirements. Populating the full official requirement text for every
standard is a data-loading exercise (proprietary/licensed catalog content in
several cases), not a code change -- the engine itself is generic and takes
new frameworks purely as data via the frameworks/requirements API.
"""
from collections.abc import Sequence
from datetime import UTC, date, datetime
from uuid import uuid4

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "202607090002"
down_revision: str | None = "202607090001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

CATALOG: list[tuple[str, str, str, str]] = [
    ("iso27001", "ISO/IEC 27001", "Information security management systems", "2022"),
    ("iso27002", "ISO/IEC 27002", "Information security controls", "2022"),
    ("iso27005", "ISO/IEC 27005", "Information security risk management", "2022"),
    ("nist-csf", "NIST Cybersecurity Framework", "NIST CSF", "2.0"),
    ("nis2", "NIS2 Directive", "EU network and information security directive", "2022"),
    ("dora", "DORA", "EU Digital Operational Resilience Act", "2022"),
    ("cis-controls", "CIS Controls", "Center for Internet Security Critical Security Controls", "8"),
    ("soc2", "SOC 2", "AICPA Trust Services Criteria", "2017"),
    ("pci-dss", "PCI DSS", "Payment Card Industry Data Security Standard", "4.0"),
    ("hipaa", "HIPAA", "Health Insurance Portability and Accountability Act Security Rule", "2013"),
]

ISO27001_REQUIREMENTS = [
    ("A.5.1", "Policies for information security", "Information security policy and topic-specific policies shall be defined, approved, published, and communicated."),
    ("A.5.7", "Threat intelligence", "Information relating to information security threats shall be collected and analysed."),
    ("A.8.1", "User endpoint devices", "Information stored on, processed by, or accessible via user endpoint devices shall be protected."),
    ("A.8.8", "Management of technical vulnerabilities", "Information about technical vulnerabilities shall be obtained and evaluated, and appropriate measures taken."),
]


def upgrade() -> None:
    op.create_table(
        "frameworks",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("code", sa.String(length=100), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("is_system", sa.Boolean(), nullable=False),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_frameworks_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="fk_frameworks_created_by_id_users", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["updated_by_id"], ["users.id"], name="fk_frameworks_updated_by_id_users", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_frameworks"),
    )
    op.create_index("ix_frameworks_organization_id", "frameworks", ["organization_id"])
    op.create_index("ix_frameworks_code", "frameworks", ["code"])

    op.create_table(
        "framework_versions",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("framework_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("version", sa.String(length=50), nullable=False),
        sa.Column("published_at", sa.Date(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["framework_id"], ["frameworks.id"], name="fk_framework_versions_framework_id_frameworks", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_framework_versions"),
        sa.UniqueConstraint("framework_id", "version", name="uq_framework_versions_framework_id_version"),
    )
    op.create_index("ix_framework_versions_framework_id", "framework_versions", ["framework_id"])

    op.create_table(
        "control_categories",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("framework_version_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("parent_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("code", sa.String(length=50), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["framework_version_id"], ["framework_versions.id"], name="fk_control_categories_framework_version_id_framework_versions", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["parent_id"], ["control_categories.id"], name="fk_control_categories_parent_id_control_categories", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_control_categories"),
    )
    op.create_index("ix_control_categories_framework_version_id", "control_categories", ["framework_version_id"])

    op.create_table(
        "requirements",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("framework_version_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("category_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("code", sa.String(length=50), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["framework_version_id"], ["framework_versions.id"], name="fk_requirements_framework_version_id_framework_versions", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["category_id"], ["control_categories.id"], name="fk_requirements_category_id_control_categories", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_requirements"),
    )
    op.create_index("ix_requirements_framework_version_id", "requirements", ["framework_version_id"])

    op.create_table(
        "control_mappings",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("control_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("requirement_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["control_id"], ["controls.id"], name="fk_control_mappings_control_id_controls", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["requirement_id"], ["requirements.id"], name="fk_control_mappings_requirement_id_requirements", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_control_mappings"),
        sa.UniqueConstraint("control_id", "requirement_id", name="uq_control_mappings_control_id_requirement_id"),
    )
    op.create_index("ix_control_mappings_control_id", "control_mappings", ["control_id"])
    op.create_index("ix_control_mappings_requirement_id", "control_mappings", ["requirement_id"])

    op.create_table(
        "assessments",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("framework_version_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column(
            "status",
            postgresql.ENUM("DRAFT", "IN_PROGRESS", "COMPLETED", "ARCHIVED", name="assessmentstatus"),
            nullable=False,
        ),
        sa.Column("period_start", sa.Date(), nullable=True),
        sa.Column("period_end", sa.Date(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("updated_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_assessments_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["framework_version_id"], ["framework_versions.id"], name="fk_assessments_framework_version_id_framework_versions", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="fk_assessments_created_by_id_users", ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["updated_by_id"], ["users.id"], name="fk_assessments_updated_by_id_users", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_assessments"),
    )
    op.create_index("ix_assessments_organization_id", "assessments", ["organization_id"])
    op.create_index("ix_assessments_framework_version_id", "assessments", ["framework_version_id"])

    op.create_table(
        "assessment_results",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("assessment_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("requirement_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "status",
            postgresql.ENUM(
                "NOT_ASSESSED", "COMPLIANT", "PARTIALLY_COMPLIANT", "NON_COMPLIANT", "NOT_APPLICABLE",
                name="requirementresultstatus",
            ),
            nullable=False,
        ),
        sa.Column("notes", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["assessment_id"], ["assessments.id"], name="fk_assessment_results_assessment_id_assessments", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["requirement_id"], ["requirements.id"], name="fk_assessment_results_requirement_id_requirements", ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name="pk_assessment_results"),
        sa.UniqueConstraint("assessment_id", "requirement_id", name="uq_assessment_results_assessment_id_requirement_id"),
    )
    op.create_index("ix_assessment_results_assessment_id", "assessment_results", ["assessment_id"])
    op.create_index("ix_assessment_results_requirement_id", "assessment_results", ["requirement_id"])

    op.create_table(
        "evidence",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("assessment_result_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("control_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("file_reference", sa.String(length=1024), nullable=False),
        sa.Column("uploaded_by_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_evidence_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["assessment_result_id"], ["assessment_results.id"], name="fk_evidence_assessment_result_id_assessment_results", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["control_id"], ["controls.id"], name="fk_evidence_control_id_controls", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["uploaded_by_id"], ["users.id"], name="fk_evidence_uploaded_by_id_users", ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id", name="pk_evidence"),
    )
    op.create_index("ix_evidence_organization_id", "evidence", ["organization_id"])
    op.create_index("ix_evidence_assessment_result_id", "evidence", ["assessment_result_id"])
    op.create_index("ix_evidence_control_id", "evidence", ["control_id"])

    op.create_table(
        "compliance_scores",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("assessment_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("framework_version_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.Column("computed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["organizations.id"], name="fk_compliance_scores_organization_id_organizations", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["assessment_id"], ["assessments.id"], name="fk_compliance_scores_assessment_id_assessments", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["framework_version_id"], ["framework_versions.id"], name="fk_compliance_scores_framework_version_id_framework_versions", ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id", name="pk_compliance_scores"),
    )
    op.create_index("ix_compliance_scores_organization_id", "compliance_scores", ["organization_id"])
    op.create_index("ix_compliance_scores_assessment_id", "compliance_scores", ["assessment_id"])

    # --- seed the framework catalog -------------------------------------------
    frameworks_table = sa.table(
        "frameworks",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("organization_id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
        sa.column("name", sa.String),
        sa.column("description", sa.Text),
        sa.column("is_system", sa.Boolean),
        sa.column("created_at", sa.DateTime(timezone=True)),
        sa.column("updated_at", sa.DateTime(timezone=True)),
    )
    framework_versions_table = sa.table(
        "framework_versions",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("framework_id", postgresql.UUID(as_uuid=True)),
        sa.column("version", sa.String),
        sa.column("published_at", sa.Date),
        sa.column("created_at", sa.DateTime(timezone=True)),
        sa.column("updated_at", sa.DateTime(timezone=True)),
    )
    requirements_table = sa.table(
        "requirements",
        sa.column("id", postgresql.UUID(as_uuid=True)),
        sa.column("framework_version_id", postgresql.UUID(as_uuid=True)),
        sa.column("code", sa.String),
        sa.column("title", sa.String),
        sa.column("description", sa.Text),
        sa.column("created_at", sa.DateTime(timezone=True)),
        sa.column("updated_at", sa.DateTime(timezone=True)),
    )

    now = datetime.now(UTC)
    today = date.today()
    framework_rows = []
    version_rows = []
    iso27001_version_id = None
    for code, name, description, version_label in CATALOG:
        framework_id = uuid4()
        version_id = uuid4()
        framework_rows.append(
            {
                "id": framework_id,
                "organization_id": None,
                "code": code,
                "name": name,
                "description": description,
                "is_system": True,
                "created_at": now,
                "updated_at": now,
            }
        )
        version_rows.append(
            {
                "id": version_id,
                "framework_id": framework_id,
                "version": version_label,
                "published_at": today,
                "created_at": now,
                "updated_at": now,
            }
        )
        if code == "iso27001":
            iso27001_version_id = version_id

    op.bulk_insert(frameworks_table, framework_rows)
    op.bulk_insert(framework_versions_table, version_rows)

    requirement_rows = [
        {
            "id": uuid4(),
            "framework_version_id": iso27001_version_id,
            "code": code,
            "title": title,
            "description": description,
            "created_at": now,
            "updated_at": now,
        }
        for code, title, description in ISO27001_REQUIREMENTS
    ]
    op.bulk_insert(requirements_table, requirement_rows)


def downgrade() -> None:
    op.drop_index("ix_compliance_scores_assessment_id", table_name="compliance_scores")
    op.drop_index("ix_compliance_scores_organization_id", table_name="compliance_scores")
    op.drop_table("compliance_scores")

    op.drop_index("ix_evidence_control_id", table_name="evidence")
    op.drop_index("ix_evidence_assessment_result_id", table_name="evidence")
    op.drop_index("ix_evidence_organization_id", table_name="evidence")
    op.drop_table("evidence")

    op.drop_index("ix_assessment_results_requirement_id", table_name="assessment_results")
    op.drop_index("ix_assessment_results_assessment_id", table_name="assessment_results")
    op.drop_table("assessment_results")

    op.drop_index("ix_assessments_framework_version_id", table_name="assessments")
    op.drop_index("ix_assessments_organization_id", table_name="assessments")
    op.drop_table("assessments")
    sa.Enum(name="requirementresultstatus").drop(op.get_bind(), checkfirst=True)
    sa.Enum(name="assessmentstatus").drop(op.get_bind(), checkfirst=True)

    op.drop_index("ix_control_mappings_requirement_id", table_name="control_mappings")
    op.drop_index("ix_control_mappings_control_id", table_name="control_mappings")
    op.drop_table("control_mappings")

    op.drop_index("ix_requirements_framework_version_id", table_name="requirements")
    op.drop_table("requirements")

    op.drop_index("ix_control_categories_framework_version_id", table_name="control_categories")
    op.drop_table("control_categories")

    op.drop_index("ix_framework_versions_framework_id", table_name="framework_versions")
    op.drop_table("framework_versions")

    op.drop_index("ix_frameworks_code", table_name="frameworks")
    op.drop_index("ix_frameworks_organization_id", table_name="frameworks")
    op.drop_table("frameworks")
