from __future__ import annotations

from datetime import datetime
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.app.modules.documents.models import (
    DocumentApprovalModel,
    DocumentModel,
    DocumentVersionModel,
)
from backend.app.modules.documents.service import (
    Document,
    DocumentApproval,
    DocumentStatus,
    DocumentType,
    DocumentVersion,
    VersionStatus,
)


def to_document(model: DocumentModel) -> Document:
    return Document(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        document_type=model.document_type,
        status=model.status,
        owner=model.owner,
        published_version_id=model.published_version_id,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_version(model: DocumentVersionModel) -> DocumentVersion:
    return DocumentVersion(
        id=model.id,
        document_id=model.document_id,
        version_number=model.version_number,
        file_reference=model.file_reference,
        change_summary=model.change_summary,
        status=model.status,
        created_by_id=model.created_by_id,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_approval(model: DocumentApprovalModel) -> DocumentApproval:
    return DocumentApproval(
        id=model.id,
        document_version_id=model.document_version_id,
        approver_id=model.approver_id,
        decision=model.decision,
        comment=model.comment,
        signature_reference=model.signature_reference,
        decided_at=model.decided_at,
        created_at=model.created_at,
    )


class SqlAlchemyDocumentRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Document]:
        statement = (
            select(DocumentModel)
            .where(DocumentModel.organization_id == organization_id, DocumentModel.deleted_at.is_(None))
            .order_by(DocumentModel.title)
        )
        rows = self._session.scalars(statement).all()
        return [to_document(row) for row in rows]

    def get_by_id(self, document_id: UUID) -> Document | None:
        model = self._session.get(DocumentModel, document_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_document(model)

    def create(
        self,
        organization_id: UUID,
        title: str,
        document_type: DocumentType,
        owner: str,
        file_reference: str,
        created_by_id: UUID | None,
    ) -> Document:
        model = DocumentModel(
            organization_id=organization_id,
            title=title,
            document_type=document_type,
            owner=owner,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_document(model)

    def set_status(self, document_id: UUID, status: DocumentStatus) -> Document:
        model = self._session.get(DocumentModel, document_id)
        if model is None:
            raise ValueError("document not found")
        model.status = status
        self._session.commit()
        self._session.refresh(model)
        return to_document(model)

    def set_published_version(self, document_id: UUID, version_id: UUID) -> Document:
        model = self._session.get(DocumentModel, document_id)
        if model is None:
            raise ValueError("document not found")
        model.published_version_id = version_id
        self._session.commit()
        self._session.refresh(model)
        return to_document(model)

    def add_version(
        self, document_id: UUID, file_reference: str, change_summary: str, created_by_id: UUID | None
    ) -> DocumentVersion:
        next_number = (
            self._session.scalar(
                select(func.coalesce(func.max(DocumentVersionModel.version_number), 0)).where(
                    DocumentVersionModel.document_id == document_id
                )
            )
            or 0
        ) + 1
        model = DocumentVersionModel(
            document_id=document_id,
            version_number=next_number,
            file_reference=file_reference,
            change_summary=change_summary,
            created_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_version(model)

    def list_versions(self, document_id: UUID) -> list[DocumentVersion]:
        statement = (
            select(DocumentVersionModel)
            .where(DocumentVersionModel.document_id == document_id)
            .order_by(DocumentVersionModel.version_number.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_version(row) for row in rows]

    def get_version(self, version_id: UUID) -> DocumentVersion | None:
        model = self._session.get(DocumentVersionModel, version_id)
        return to_version(model) if model else None

    def set_version_status(self, version_id: UUID, status: VersionStatus) -> DocumentVersion:
        model = self._session.get(DocumentVersionModel, version_id)
        if model is None:
            raise ValueError("document version not found")
        model.status = status
        self._session.commit()
        self._session.refresh(model)
        return to_version(model)

    def record_approval(
        self,
        document_version_id: UUID,
        approver_id: UUID,
        decision: VersionStatus,
        comment: str,
        signature_reference: str | None,
        decided_at: datetime,
    ) -> DocumentApproval:
        model = DocumentApprovalModel(
            document_version_id=document_version_id,
            approver_id=approver_id,
            decision=decision,
            comment=comment,
            signature_reference=signature_reference,
            decided_at=decided_at,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_approval(model)

    def list_approvals(self, document_version_id: UUID) -> list[DocumentApproval]:
        statement = select(DocumentApprovalModel).where(
            DocumentApprovalModel.document_version_id == document_version_id
        )
        rows = self._session.scalars(statement).all()
        return [to_approval(row) for row in rows]
