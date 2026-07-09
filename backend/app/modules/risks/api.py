from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_risk_service,
    require_permission,
)
from backend.app.modules.risks.schemas import RiskCreate, RiskRead
from backend.app.modules.risks.service import CreateRiskCommand, RiskService
from backend.app.modules.users.service import User
from backend.app.security.permissions import RISKS_MANAGE, RISKS_READ
from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.get(
    "",
    response_model=list[RiskRead],
    dependencies=[Depends(require_permission(RISKS_READ))],
)
def list_risks(
    current_user: User = Depends(get_current_user),
    service: RiskService = Depends(get_risk_service),
) -> list[RiskRead]:
    return [
        RiskRead.model_validate(item)
        for item in service.list_risks(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=RiskRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(RISKS_MANAGE))],
)
def create_risk(
    payload: RiskCreate,
    current_user: User = Depends(get_current_user),
    service: RiskService = Depends(get_risk_service),
) -> RiskRead:
    risk = service.create_risk(
        CreateRiskCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return RiskRead.model_validate(risk)
