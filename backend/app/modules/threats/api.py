from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_threat_service,
    require_permission,
)
from backend.app.modules.threats.schemas import ThreatCreate, ThreatRead
from backend.app.modules.threats.service import CreateThreatCommand, ThreatService
from backend.app.modules.users.service import User
from backend.app.security.permissions import THREATS_MANAGE, THREATS_READ
from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.get(
    "",
    response_model=list[ThreatRead],
    dependencies=[Depends(require_permission(THREATS_READ))],
)
def list_threats(
    current_user: User = Depends(get_current_user),
    service: ThreatService = Depends(get_threat_service),
) -> list[ThreatRead]:
    return [ThreatRead.model_validate(item) for item in service.list_threats(current_user.organization_id)]


@router.post(
    "",
    response_model=ThreatRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(THREATS_MANAGE))],
)
def create_threat(
    payload: ThreatCreate,
    current_user: User = Depends(get_current_user),
    service: ThreatService = Depends(get_threat_service),
) -> ThreatRead:
    threat = service.create_threat(
        CreateThreatCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return ThreatRead.model_validate(threat)
