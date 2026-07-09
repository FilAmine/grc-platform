from datetime import date, datetime
from uuid import UUID as PyUUID

from sqlalchemy import Date, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.audits.service import (
    AuditStatus,
    ChecklistItemStatus,
    CorrectiveActionStatus,
    FindingSeverity,
    FindingStatus,
)


class AuditModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "audits"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    scope: Mapped[str] = mapped_column(Text, nullable=False, default="")
    lead_auditor: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[AuditStatus] = mapped_column(Enum(AuditStatus), default=AuditStatus.PLANNED, nullable=False)
    period_start: Mapped[date | None] = mapped_column(Date, nullable=True)
    period_end: Mapped[date | None] = mapped_column(Date, nullable=True)

    checklist_items: Mapped[list["ChecklistItemModel"]] = relationship(
        "ChecklistItemModel", back_populates="audit"
    )
    findings: Mapped[list["FindingModel"]] = relationship("FindingModel", back_populates="audit")


class ChecklistItemModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "checklist_items"

    audit_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("audits.id", ondelete="CASCADE"), index=True, nullable=False
    )
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[ChecklistItemStatus] = mapped_column(
        Enum(ChecklistItemStatus), default=ChecklistItemStatus.PENDING, nullable=False
    )
    notes: Mapped[str] = mapped_column(Text, nullable=False, default="")

    audit: Mapped["AuditModel"] = relationship("AuditModel", back_populates="checklist_items")


class FindingModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "findings"

    audit_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("audits.id", ondelete="CASCADE"), index=True, nullable=False
    )
    checklist_item_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("checklist_items.id", ondelete="SET NULL"), nullable=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    severity: Mapped[FindingSeverity] = mapped_column(Enum(FindingSeverity), nullable=False)
    status: Mapped[FindingStatus] = mapped_column(
        Enum(FindingStatus), default=FindingStatus.OPEN, nullable=False
    )

    audit: Mapped["AuditModel"] = relationship("AuditModel", back_populates="findings")
    corrective_actions: Mapped[list["CorrectiveActionModel"]] = relationship(
        "CorrectiveActionModel", back_populates="finding"
    )


class CorrectiveActionModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "corrective_actions"

    finding_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("findings.id", ondelete="CASCADE"), index=True, nullable=False
    )
    description: Mapped[str] = mapped_column(Text, nullable=False)
    owner: Mapped[str] = mapped_column(String(255), nullable=False)
    due_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    status: Mapped[CorrectiveActionStatus] = mapped_column(
        Enum(CorrectiveActionStatus), default=CorrectiveActionStatus.OPEN, nullable=False
    )
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    finding: Mapped["FindingModel"] = relationship("FindingModel", back_populates="corrective_actions")
