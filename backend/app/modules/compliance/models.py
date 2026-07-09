"""Generic compliance engine persistence models.

Frameworks are data, not code: ISO 27001, NIST CSF, SOC 2, etc. are all rows in
``frameworks``/``framework_versions``/``requirements``. Supporting a new standard
means loading rows, never touching this module.
"""

from datetime import date, datetime
from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.compliance.service import AssessmentStatus, RequirementResultStatus
from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class FrameworkModel(UUIDPKMixin, TimestampMixin, AuditColumnsMixin, Base):
    """Either a system-wide catalog entry (``organization_id`` is ``NULL``, e.g. the
    seeded ISO 27001 entry) or a tenant's private custom framework."""

    __tablename__ = "frameworks"

    organization_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True
    )
    code: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    is_system: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    versions: Mapped[list["FrameworkVersionModel"]] = relationship(
        "FrameworkVersionModel", back_populates="framework"
    )


class FrameworkVersionModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "framework_versions"
    __table_args__ = (UniqueConstraint("framework_id", "version", name="uq_framework_versions_framework_id_version"),)

    framework_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("frameworks.id", ondelete="CASCADE"), index=True, nullable=False
    )
    version: Mapped[str] = mapped_column(String(50), nullable=False)
    published_at: Mapped[date | None] = mapped_column(Date, nullable=True)

    framework: Mapped["FrameworkModel"] = relationship("FrameworkModel", back_populates="versions")
    categories: Mapped[list["ControlCategoryModel"]] = relationship(
        "ControlCategoryModel", back_populates="framework_version"
    )
    requirements: Mapped[list["RequirementModel"]] = relationship(
        "RequirementModel", back_populates="framework_version"
    )


class ControlCategoryModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "control_categories"

    framework_version_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("framework_versions.id", ondelete="CASCADE"), index=True, nullable=False
    )
    parent_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("control_categories.id", ondelete="CASCADE"), nullable=True
    )
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    framework_version: Mapped["FrameworkVersionModel"] = relationship(
        "FrameworkVersionModel", back_populates="categories"
    )


class RequirementModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "requirements"

    framework_version_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("framework_versions.id", ondelete="CASCADE"), index=True, nullable=False
    )
    category_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("control_categories.id", ondelete="SET NULL"), nullable=True
    )
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")

    framework_version: Mapped["FrameworkVersionModel"] = relationship(
        "FrameworkVersionModel", back_populates="requirements"
    )


class ControlMappingModel(UUIDPKMixin, TimestampMixin, Base):
    """Links one of an organization's own controls to a (global or custom) requirement
    it is intended to satisfy."""

    __tablename__ = "control_mappings"
    __table_args__ = (
        UniqueConstraint("control_id", "requirement_id", name="uq_control_mappings_control_id_requirement_id"),
    )

    control_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("controls.id", ondelete="CASCADE"), index=True, nullable=False
    )
    requirement_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("requirements.id", ondelete="CASCADE"), index=True, nullable=False
    )


class AssessmentModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "assessments"

    framework_version_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("framework_versions.id", ondelete="RESTRICT"), index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[AssessmentStatus] = mapped_column(
        Enum(AssessmentStatus), default=AssessmentStatus.DRAFT, nullable=False
    )
    period_start: Mapped[date | None] = mapped_column(Date, nullable=True)
    period_end: Mapped[date | None] = mapped_column(Date, nullable=True)

    results: Mapped[list["AssessmentResultModel"]] = relationship(
        "AssessmentResultModel", back_populates="assessment"
    )


class AssessmentResultModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "assessment_results"
    __table_args__ = (
        UniqueConstraint("assessment_id", "requirement_id", name="uq_assessment_results_assessment_id_requirement_id"),
    )

    assessment_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("assessments.id", ondelete="CASCADE"), index=True, nullable=False
    )
    requirement_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("requirements.id", ondelete="CASCADE"), index=True, nullable=False
    )
    status: Mapped[RequirementResultStatus] = mapped_column(
        Enum(RequirementResultStatus), default=RequirementResultStatus.NOT_ASSESSED, nullable=False
    )
    notes: Mapped[str] = mapped_column(Text, nullable=False, default="")

    assessment: Mapped["AssessmentModel"] = relationship("AssessmentModel", back_populates="results")


class EvidenceModel(UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, Base):
    __tablename__ = "evidence"

    assessment_result_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("assessment_results.id", ondelete="CASCADE"), nullable=True, index=True
    )
    control_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("controls.id", ondelete="CASCADE"), nullable=True, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    file_reference: Mapped[str] = mapped_column(String(1024), nullable=False)
    uploaded_by_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )


class ComplianceScoreModel(UUIDPKMixin, TenantScopedMixin, TimestampMixin, Base):
    __tablename__ = "compliance_scores"

    assessment_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("assessments.id", ondelete="CASCADE"), index=True, nullable=False
    )
    framework_version_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("framework_versions.id", ondelete="RESTRICT"), nullable=False
    )
    score: Mapped[float] = mapped_column(Float, nullable=False)
    computed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
