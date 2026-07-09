from datetime import UTC, datetime
from uuid import UUID

from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_document_service,
    require_permission,
)
from backend.app.modules.documents.schemas import (
    ApprovalDecision,
    ApprovalRead,
    DocumentCreate,
    DocumentRead,
    VersionCreate,
    VersionRead,
)
from backend.app.modules.documents.service import (
    CreateDocumentCommand,
    CreateVersionCommand,
    Document,
    DocumentNotFoundError,
    DocumentService,
    InvalidApprovalDecisionError,
)
from backend.app.modules.users.service import User
from backend.app.security.permissions import DOCUMENTS_MANAGE, DOCUMENTS_READ
from backend.app.workflow.state_machine import IllegalTransitionError
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


def _owned_document(document_id: UUID, current_user: User, service: DocumentService) -> Document:
    document = service.get_document(document_id)
    if document is None or document.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="document not found")
    return document


@router.get("", response_model=list[DocumentRead], dependencies=[Depends(require_permission(DOCUMENTS_READ))])
def list_documents(
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> list[DocumentRead]:
    return [DocumentRead.model_validate(d) for d in service.list_documents(current_user.organization_id)]


@router.post(
    "", response_model=DocumentRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(DOCUMENTS_MANAGE))],
)
def create_document(
    payload: DocumentCreate,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> DocumentRead:
    document = service.create_document(
        CreateDocumentCommand(
            organization_id=current_user.organization_id, created_by_id=current_user.id, **payload.model_dump()
        )
    )
    return DocumentRead.model_validate(document)


@router.get(
    "/{document_id}", response_model=DocumentRead, dependencies=[Depends(require_permission(DOCUMENTS_READ))]
)
def get_document(
    document_id: UUID,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> DocumentRead:
    return DocumentRead.model_validate(_owned_document(document_id, current_user, service))


@router.post(
    "/{document_id}/archive", response_model=DocumentRead,
    dependencies=[Depends(require_permission(DOCUMENTS_MANAGE))],
)
def archive_document(
    document_id: UUID,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> DocumentRead:
    _owned_document(document_id, current_user, service)
    try:
        document = service.archive_document(document_id)
    except IllegalTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return DocumentRead.model_validate(document)


@router.get(
    "/{document_id}/versions", response_model=list[VersionRead],
    dependencies=[Depends(require_permission(DOCUMENTS_READ))],
)
def list_versions(
    document_id: UUID,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> list[VersionRead]:
    _owned_document(document_id, current_user, service)
    return [VersionRead.model_validate(v) for v in service.list_versions(document_id)]


@router.post(
    "/{document_id}/versions", response_model=VersionRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(DOCUMENTS_MANAGE))],
)
def create_version(
    document_id: UUID,
    payload: VersionCreate,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> VersionRead:
    _owned_document(document_id, current_user, service)
    version = service.add_version(
        CreateVersionCommand(document_id=document_id, created_by_id=current_user.id, **payload.model_dump())
    )
    return VersionRead.model_validate(version)


def _owned_version(version_id: UUID, current_user: User, service: DocumentService):
    version = service.get_version(version_id)
    if version is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="version not found")
    _owned_document(version.document_id, current_user, service)
    return version


@router.post(
    "/versions/{version_id}/submit-for-approval", response_model=VersionRead,
    dependencies=[Depends(require_permission(DOCUMENTS_MANAGE))],
)
def submit_for_approval(
    version_id: UUID,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> VersionRead:
    _owned_version(version_id, current_user, service)
    try:
        version = service.submit_for_approval(version_id)
    except IllegalTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return VersionRead.model_validate(version)


@router.post(
    "/versions/{version_id}/approval", response_model=ApprovalRead,
    dependencies=[Depends(require_permission(DOCUMENTS_MANAGE))],
)
def decide_approval(
    version_id: UUID,
    payload: ApprovalDecision,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> ApprovalRead:
    _owned_version(version_id, current_user, service)
    try:
        approval = service.decide_approval(
            version_id,
            current_user.id,
            payload.approve,
            payload.comment,
            payload.signature_reference,
            datetime.now(UTC),
        )
    except DocumentNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except InvalidApprovalDecisionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return ApprovalRead.model_validate(approval)


@router.get(
    "/versions/{version_id}/approvals", response_model=list[ApprovalRead],
    dependencies=[Depends(require_permission(DOCUMENTS_READ))],
)
def list_approvals(
    version_id: UUID,
    current_user: User = Depends(get_current_user),
    service: DocumentService = Depends(get_document_service),
) -> list[ApprovalRead]:
    _owned_version(version_id, current_user, service)
    return [ApprovalRead.model_validate(a) for a in service.list_approvals(version_id)]
