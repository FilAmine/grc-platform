from datetime import datetime
from uuid import UUID as PyUUID

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
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
from backend.app.modules.documents.service import DocumentStatus, DocumentType, VersionStatus


class DocumentModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "documents"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    document_type: Mapped[DocumentType] = mapped_column(Enum(DocumentType), nullable=False)
    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus), default=DocumentStatus.DRAFT, nullable=False
    )
    owner: Mapped[str] = mapped_column(String(255), nullable=False)
    published_version_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("document_versions.id", ondelete="SET NULL", use_alter=True), nullable=True
    )

    versions: Mapped[list["DocumentVersionModel"]] = relationship(
        "DocumentVersionModel", back_populates="document", foreign_keys="DocumentVersionModel.document_id"
    )


class DocumentVersionModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "document_versions"

    document_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("documents.id", ondelete="CASCADE"), index=True, nullable=False
    )
    version_number: Mapped[int] = mapped_column(Integer, nullable=False)
    file_reference: Mapped[str] = mapped_column(String(1024), nullable=False)
    change_summary: Mapped[str] = mapped_column(Text, nullable=False, default="")
    status: Mapped[VersionStatus] = mapped_column(
        Enum(VersionStatus), default=VersionStatus.DRAFT, nullable=False
    )
    created_by_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )

    document: Mapped["DocumentModel"] = relationship(
        "DocumentModel", back_populates="versions", foreign_keys=[document_id]
    )


class DocumentApprovalModel(UUIDPKMixin, TimestampMixin, Base):
    """``signature_reference`` is a placeholder slot for an external e-signature
    provider's envelope/reference id -- wiring an actual provider is future work,
    but the schema already has somewhere to put it."""

    __tablename__ = "document_approvals"

    document_version_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("document_versions.id", ondelete="CASCADE"), index=True, nullable=False
    )
    approver_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    decision: Mapped[VersionStatus] = mapped_column(Enum(VersionStatus), nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False, default="")
    signature_reference: Mapped[str | None] = mapped_column(String(255), nullable=True)
    decided_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
