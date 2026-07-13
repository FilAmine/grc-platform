from backend.app.interfaces.api.dependencies import get_current_user, get_risk_source_service, require_permission
from backend.app.modules.risk_sources.schemas import RiskSourceCreate, RiskSourceRead
from backend.app.modules.risk_sources.service import CreateRiskSourceCommand, RiskSourceService
from backend.app.modules.users.service import User
from backend.app.security.permissions import RISK_SOURCES_MANAGE, RISK_SOURCES_READ
from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.get(
    "",
    response_model=list[RiskSourceRead],
    dependencies=[Depends(require_permission(RISK_SOURCES_READ))],
)
def list_risk_sources(
    current_user: User = Depends(get_current_user),
    service: RiskSourceService = Depends(get_risk_source_service),
) -> list[RiskSourceRead]:
    return [
        RiskSourceRead.model_validate(item)
        for item in service.list_risk_sources(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=RiskSourceRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(RISK_SOURCES_MANAGE))],
)
def create_risk_source(
    payload: RiskSourceCreate,
    current_user: User = Depends(get_current_user),
    service: RiskSourceService = Depends(get_risk_source_service),
) -> RiskSourceRead:
    risk_source = service.create_risk_source(
        CreateRiskSourceCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return RiskSourceRead.model_validate(risk_source)
