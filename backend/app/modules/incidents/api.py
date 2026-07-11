from datetime import UTC, datetime
from uuid import UUID

from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_incident_service,
    require_permission,
)
from backend.app.modules.incidents.schemas import IncidentCreate, IncidentRead, IncidentStatusUpdate
from backend.app.modules.incidents.service import CreateIncidentCommand, Incident, IncidentService
from backend.app.modules.users.service import User
from backend.app.security.permissions import INCIDENTS_MANAGE, INCIDENTS_READ
from backend.app.workflow.state_machine import IllegalTransitionError
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


def _owned_incident(incident_id: UUID, current_user: User, service: IncidentService) -> Incident:
    incident = service.get_incident(incident_id)
    if incident is None or incident.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="incident not found")
    return incident


@router.get(
    "",
    response_model=list[IncidentRead],
    dependencies=[Depends(require_permission(INCIDENTS_READ))],
)
def list_incidents(
    current_user: User = Depends(get_current_user),
    service: IncidentService = Depends(get_incident_service),
) -> list[IncidentRead]:
    return [
        IncidentRead.model_validate(item)
        for item in service.list_incidents(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=IncidentRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(INCIDENTS_MANAGE))],
)
def create_incident(
    payload: IncidentCreate,
    current_user: User = Depends(get_current_user),
    service: IncidentService = Depends(get_incident_service),
) -> IncidentRead:
    incident = service.create_incident(
        CreateIncidentCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return IncidentRead.model_validate(incident)


@router.get(
    "/{incident_id}",
    response_model=IncidentRead,
    dependencies=[Depends(require_permission(INCIDENTS_READ))],
)
def get_incident(
    incident_id: UUID,
    current_user: User = Depends(get_current_user),
    service: IncidentService = Depends(get_incident_service),
) -> IncidentRead:
    incident = _owned_incident(incident_id, current_user, service)
    return IncidentRead.model_validate(incident)


@router.patch(
    "/{incident_id}/status",
    response_model=IncidentRead,
    dependencies=[Depends(require_permission(INCIDENTS_MANAGE))],
)
def update_incident_status(
    incident_id: UUID,
    payload: IncidentStatusUpdate,
    current_user: User = Depends(get_current_user),
    service: IncidentService = Depends(get_incident_service),
) -> IncidentRead:
    _owned_incident(incident_id, current_user, service)
    try:
        incident = service.set_status(incident_id, payload.status, datetime.now(UTC))
    except IllegalTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return IncidentRead.model_validate(incident)
