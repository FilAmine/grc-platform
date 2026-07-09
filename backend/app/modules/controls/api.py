from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from backend.app.interfaces.api.dependencies import get_control_service
from backend.app.modules.controls.schemas import ControlCreate, ControlRead
from backend.app.modules.controls.service import ControlService, CreateControlCommand

router = APIRouter()


@router.get("", response_model=list[ControlRead])
def list_controls(
    organization_id: UUID | None = Query(default=None),
    service: ControlService = Depends(get_control_service),
) -> list[ControlRead]:
    return [ControlRead.model_validate(item) for item in service.list_controls(organization_id)]


@router.post("", response_model=ControlRead, status_code=status.HTTP_201_CREATED)
def create_control(
    payload: ControlCreate,
    service: ControlService = Depends(get_control_service),
) -> ControlRead:
    control = service.create_control(CreateControlCommand(**payload.model_dump()))
    return ControlRead.model_validate(control)
