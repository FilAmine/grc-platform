from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class DocumentType(StrEnum):
    POLICY = "policy"
    PROCEDURE = "procedure"
    STANDARD = "standard"
    GUIDELINE = "guideline"
    TEMPLATE = "template"


class DocumentStatus(StrEnum):
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class VersionStatus(StrEnum):
    DRAFT = "draft"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass(frozen=True)
class Document:
    id: UUID
    organization_id: UUID
    title: str
    document_type: DocumentType
    status: DocumentStatus
    owner: str
    published_version_id: UUID | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class DocumentVersion:
    id: UUID
    document_id: UUID
    version_number: int
    file_reference: str
    change_summary: str
    status: VersionStatus
    created_by_id: UUID | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class DocumentApproval:
    id: UUID
    document_version_id: UUID
    approver_id: UUID
    decision: VersionStatus
    comment: str
    signature_reference: str | None
    decided_at: datetime | None
    created_at: datetime


@dataclass(frozen=True)
class CreateDocumentCommand:
    organization_id: UUID
    title: str
    document_type: DocumentType
    owner: str
    file_reference: str
    created_by_id: UUID | None = None


@dataclass(frozen=True)
class CreateVersionCommand:
    document_id: UUID
    file_reference: str
    change_summary: str = ""
    created_by_id: UUID | None = None


class DocumentStore(Protocol):
    def list(self, organization_id: UUID) -> list[Document]:
        raise NotImplementedError

    def get_by_id(self, document_id: UUID) -> Document | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        title: str,
        document_type: DocumentType,
        owner: str,
        file_reference: str,
        created_by_id: UUID | None,
    ) -> Document:
        raise NotImplementedError

    def set_status(self, document_id: UUID, status: DocumentStatus) -> Document:
        raise NotImplementedError

    def set_published_version(self, document_id: UUID, version_id: UUID) -> Document:
        raise NotImplementedError

    def add_version(
        self, document_id: UUID, file_reference: str, change_summary: str, created_by_id: UUID | None
    ) -> DocumentVersion:
        raise NotImplementedError

    def list_versions(self, document_id: UUID) -> list[DocumentVersion]:
        raise NotImplementedError

    def get_version(self, version_id: UUID) -> DocumentVersion | None:
        raise NotImplementedError

    def set_version_status(self, version_id: UUID, status: VersionStatus) -> DocumentVersion:
        raise NotImplementedError

    def record_approval(
        self,
        document_version_id: UUID,
        approver_id: UUID,
        decision: VersionStatus,
        comment: str,
        signature_reference: str | None,
        decided_at: datetime,
    ) -> DocumentApproval:
        raise NotImplementedError

    def list_approvals(self, document_version_id: UUID) -> list[DocumentApproval]:
        raise NotImplementedError


class DocumentNotFoundError(Exception):
    pass


class InvalidApprovalDecisionError(Exception):
    pass


class DocumentService:
    def __init__(self, documents: DocumentStore) -> None:
        self._documents = documents

    def list_documents(self, organization_id: UUID) -> list[Document]:
        return self._documents.list(organization_id)

    def get_document(self, document_id: UUID) -> Document | None:
        return self._documents.get_by_id(document_id)

    def create_document(self, command: CreateDocumentCommand) -> Document:
        document = self._documents.create(
            organization_id=command.organization_id,
            title=command.title,
            document_type=command.document_type,
            owner=command.owner,
            file_reference=command.file_reference,
            created_by_id=command.created_by_id,
        )
        self._documents.add_version(document.id, command.file_reference, "initial version", command.created_by_id)
        return document

    def add_version(self, command: CreateVersionCommand) -> DocumentVersion:
        return self._documents.add_version(
            command.document_id, command.file_reference, command.change_summary, command.created_by_id
        )

    def list_versions(self, document_id: UUID) -> list[DocumentVersion]:
        return self._documents.list_versions(document_id)

    def get_version(self, version_id: UUID) -> DocumentVersion | None:
        return self._documents.get_version(version_id)

    def submit_for_approval(self, version_id: UUID) -> DocumentVersion:
        return self._documents.set_version_status(version_id, VersionStatus.PENDING_APPROVAL)

    def decide_approval(
        self,
        version_id: UUID,
        approver_id: UUID,
        approve: bool,
        comment: str,
        signature_reference: str | None,
        now: datetime,
    ) -> DocumentApproval:
        version = self._documents.get_version(version_id)
        if version is None:
            raise DocumentNotFoundError("document version not found")
        if version.status != VersionStatus.PENDING_APPROVAL:
            raise InvalidApprovalDecisionError("version is not pending approval")

        decision = VersionStatus.APPROVED if approve else VersionStatus.REJECTED
        approval = self._documents.record_approval(
            version_id, approver_id, decision, comment, signature_reference, now
        )
        self._documents.set_version_status(version_id, decision)
        if approve:
            self._documents.set_published_version(version.document_id, version_id)
            self._documents.set_status(version.document_id, DocumentStatus.PUBLISHED)
        return approval

    def list_approvals(self, document_version_id: UUID) -> list[DocumentApproval]:
        return self._documents.list_approvals(document_version_id)

    def archive_document(self, document_id: UUID) -> Document:
        return self._documents.set_status(document_id, DocumentStatus.ARCHIVED)
