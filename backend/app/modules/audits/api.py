from datetime import UTC, datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from backend.app.interfaces.api.dependencies import get_audit_service, get_current_user, require_permission
from backend.app.modules.audits.schemas import (
    AuditCreate,
    AuditRead,
    AuditReportRead,
    AuditStatusUpdate,
    ChecklistItemCreate,
    ChecklistItemRead,
    ChecklistItemStatusUpdate,
    CorrectiveActionCreate,
    CorrectiveActionRead,
    CorrectiveActionStatusUpdate,
    FindingCreate,
    FindingRead,
    FindingStatusUpdate,
)
from backend.app.modules.audits.service import (
    Audit,
    AuditService,
    CreateAuditCommand,
    CreateChecklistItemCommand,
    CreateCorrectiveActionCommand,
    CreateFindingCommand,
)
from backend.app.modules.users.service import User
from backend.app.security.permissions import AUDITS_MANAGE, AUDITS_READ
from backend.app.workflow.state_machine import IllegalTransitionError

router = APIRouter()


def _owned_audit(audit_id: UUID, current_user: User, service: AuditService) -> Audit:
    audit = service.get_audit(audit_id)
    if audit is None or audit.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="audit not found")
    return audit


def _owned_finding(finding_id: UUID, current_user: User, service: AuditService):
    finding = service.get_finding(finding_id)
    if finding is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="finding not found")
    _owned_audit(finding.audit_id, current_user, service)
    return finding


@router.get("", response_model=list[AuditRead], dependencies=[Depends(require_permission(AUDITS_READ))])
def list_audits(
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> list[AuditRead]:
    return [AuditRead.model_validate(a) for a in service.list_audits(current_user.organization_id)]


@router.post(
    "", response_model=AuditRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AUDITS_MANAGE))],
)
def create_audit(
    payload: AuditCreate,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> AuditRead:
    audit = service.create_audit(
        CreateAuditCommand(
            organization_id=current_user.organization_id, created_by_id=current_user.id, **payload.model_dump()
        )
    )
    return AuditRead.model_validate(audit)


@router.get("/{audit_id}", response_model=AuditRead, dependencies=[Depends(require_permission(AUDITS_READ))])
def get_audit(
    audit_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> AuditRead:
    return AuditRead.model_validate(_owned_audit(audit_id, current_user, service))


@router.patch(
    "/{audit_id}/status", response_model=AuditRead, dependencies=[Depends(require_permission(AUDITS_MANAGE))]
)
def update_audit_status(
    audit_id: UUID,
    payload: AuditStatusUpdate,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> AuditRead:
    _owned_audit(audit_id, current_user, service)
    try:
        audit = service.set_status(audit_id, payload.status)
    except IllegalTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return AuditRead.model_validate(audit)


@router.get(
    "/{audit_id}/report", response_model=AuditReportRead, dependencies=[Depends(require_permission(AUDITS_READ))]
)
def get_audit_report(
    audit_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> AuditReportRead:
    _owned_audit(audit_id, current_user, service)
    report = service.build_report(audit_id)
    assert report is not None
    return AuditReportRead.model_validate(report, from_attributes=True)


@router.get(
    "/{audit_id}/checklist-items",
    response_model=list[ChecklistItemRead],
    dependencies=[Depends(require_permission(AUDITS_READ))],
)
def list_checklist_items(
    audit_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> list[ChecklistItemRead]:
    _owned_audit(audit_id, current_user, service)
    return [ChecklistItemRead.model_validate(i) for i in service.list_checklist_items(audit_id)]


@router.post(
    "/{audit_id}/checklist-items",
    response_model=ChecklistItemRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AUDITS_MANAGE))],
)
def create_checklist_item(
    audit_id: UUID,
    payload: ChecklistItemCreate,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> ChecklistItemRead:
    _owned_audit(audit_id, current_user, service)
    item = service.add_checklist_item(CreateChecklistItemCommand(audit_id=audit_id, description=payload.description))
    return ChecklistItemRead.model_validate(item)


@router.put(
    "/checklist-items/{item_id}/status",
    response_model=ChecklistItemRead,
    dependencies=[Depends(require_permission(AUDITS_MANAGE))],
)
def update_checklist_item_status(
    item_id: UUID,
    payload: ChecklistItemStatusUpdate,
    service: AuditService = Depends(get_audit_service),
) -> ChecklistItemRead:
    item = service.set_checklist_item_status(item_id, payload.status, payload.notes)
    return ChecklistItemRead.model_validate(item)


@router.get(
    "/{audit_id}/findings", response_model=list[FindingRead], dependencies=[Depends(require_permission(AUDITS_READ))]
)
def list_findings(
    audit_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> list[FindingRead]:
    _owned_audit(audit_id, current_user, service)
    return [FindingRead.model_validate(f) for f in service.list_findings(audit_id)]


@router.post(
    "/{audit_id}/findings",
    response_model=FindingRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AUDITS_MANAGE))],
)
def create_finding(
    audit_id: UUID,
    payload: FindingCreate,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> FindingRead:
    _owned_audit(audit_id, current_user, service)
    finding = service.add_finding(CreateFindingCommand(audit_id=audit_id, **payload.model_dump()))
    return FindingRead.model_validate(finding)


@router.patch(
    "/findings/{finding_id}/status",
    response_model=FindingRead,
    dependencies=[Depends(require_permission(AUDITS_MANAGE))],
)
def update_finding_status(
    finding_id: UUID,
    payload: FindingStatusUpdate,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> FindingRead:
    _owned_finding(finding_id, current_user, service)
    return FindingRead.model_validate(service.set_finding_status(finding_id, payload.status))


@router.get(
    "/findings/{finding_id}/corrective-actions",
    response_model=list[CorrectiveActionRead],
    dependencies=[Depends(require_permission(AUDITS_READ))],
)
def list_corrective_actions(
    finding_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> list[CorrectiveActionRead]:
    _owned_finding(finding_id, current_user, service)
    return [CorrectiveActionRead.model_validate(a) for a in service.list_corrective_actions(finding_id)]


@router.post(
    "/findings/{finding_id}/corrective-actions",
    response_model=CorrectiveActionRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AUDITS_MANAGE))],
)
def create_corrective_action(
    finding_id: UUID,
    payload: CorrectiveActionCreate,
    current_user: User = Depends(get_current_user),
    service: AuditService = Depends(get_audit_service),
) -> CorrectiveActionRead:
    _owned_finding(finding_id, current_user, service)
    action = service.add_corrective_action(
        CreateCorrectiveActionCommand(finding_id=finding_id, **payload.model_dump())
    )
    return CorrectiveActionRead.model_validate(action)


@router.patch(
    "/corrective-actions/{action_id}/status",
    response_model=CorrectiveActionRead,
    dependencies=[Depends(require_permission(AUDITS_MANAGE))],
)
def update_corrective_action_status(
    action_id: UUID,
    payload: CorrectiveActionStatusUpdate,
    service: AuditService = Depends(get_audit_service),
) -> CorrectiveActionRead:
    action = service.set_corrective_action_status(action_id, payload.status, datetime.now(UTC))
    return CorrectiveActionRead.model_validate(action)
