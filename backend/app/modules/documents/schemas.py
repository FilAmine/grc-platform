from datetime import datetime
from uuid import UUID

from pydantic import Field

from backend.app.common.schemas import ReadSchema
from backend.app.modules.documents.service import DocumentStatus, DocumentType, VersionStatus


class DocumentCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    document_type: DocumentType
    owner: str = Field(min_length=2, max_length=255)
    file_reference: str = Field(min_length=1, max_length=1024)


class DocumentRead(ReadSchema):
    id: UUID
    organization_id: UUID
    title: str
    document_type: DocumentType
    status: DocumentStatus
    owner: str
    published_version_id: UUID | None
    created_at: datetime
    updated_at: datetime


class VersionCreate(ReadSchema):
    file_reference: str = Field(min_length=1, max_length=1024)
    change_summary: str = Field(default="", max_length=4000)


class VersionRead(ReadSchema):
    id: UUID
    document_id: UUID
    version_number: int
    file_reference: str
    change_summary: str
    status: VersionStatus
    created_by_id: UUID | None
    created_at: datetime
    updated_at: datetime


class ApprovalDecision(ReadSchema):
    approve: bool
    comment: str = Field(default="", max_length=4000)
    signature_reference: str | None = None


class ApprovalRead(ReadSchema):
    id: UUID
    document_version_id: UUID
    approver_id: UUID
    decision: VersionStatus
    comment: str
    signature_reference: str | None
    decided_at: datetime | None
    created_at: datetime
