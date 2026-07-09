from fastapi import APIRouter, Depends, status

from backend.app.interfaces.api.dependencies import get_control_service, get_current_user, require_permission
from backend.app.modules.controls.schemas import ControlCreate, ControlRead
from backend.app.modules.controls.service import ControlService, CreateControlCommand
from backend.app.modules.users.service import User
from backend.app.security.permissions import CONTROLS_MANAGE, CONTROLS_READ

router = APIRouter()


@router.get(
    "",
    response_model=list[ControlRead],
    dependencies=[Depends(require_permission(CONTROLS_READ))],
)
def list_controls(
    current_user: User = Depends(get_current_user),
    service: ControlService = Depends(get_control_service),
) -> list[ControlRead]:
    return [
        ControlRead.model_validate(item)
        for item in service.list_controls(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=ControlRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(CONTROLS_MANAGE))],
)
def create_control(
    payload: ControlCreate,
    current_user: User = Depends(get_current_user),
    service: ControlService = Depends(get_control_service),
) -> ControlRead:
    control = service.create_control(
        CreateControlCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return ControlRead.model_validate(control)
