from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_feared_event_service,
    get_risk_origin_service,
    get_risk_source_service,
    require_permission,
)
from backend.app.modules.feared_events.service import FearedEventService
from backend.app.modules.risk_origins.schemas import RiskOriginCreate, RiskOriginRead
from backend.app.modules.risk_origins.service import CreateRiskOriginCommand, RiskOriginService
from backend.app.modules.risk_sources.service import RiskSourceService
from backend.app.modules.users.service import User
from backend.app.security.permissions import RISK_ORIGINS_MANAGE, RISK_ORIGINS_READ
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "",
    response_model=list[RiskOriginRead],
    dependencies=[Depends(require_permission(RISK_ORIGINS_READ))],
)
def list_risk_origins(
    current_user: User = Depends(get_current_user),
    service: RiskOriginService = Depends(get_risk_origin_service),
) -> list[RiskOriginRead]:
    return [
        RiskOriginRead.model_validate(item)
        for item in service.list_risk_origins(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=RiskOriginRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(RISK_ORIGINS_MANAGE))],
)
def create_risk_origin(
    payload: RiskOriginCreate,
    current_user: User = Depends(get_current_user),
    service: RiskOriginService = Depends(get_risk_origin_service),
    risk_source_service: RiskSourceService = Depends(get_risk_source_service),
    feared_event_service: FearedEventService = Depends(get_feared_event_service),
) -> RiskOriginRead:
    # Same cross-tenant validation pattern as risks/api.py's optional-FK
    # checks: a foreign key proves "some row exists," not "same tenant."
    risk_source = risk_source_service.get_risk_source(payload.risk_source_id)
    if risk_source is None or risk_source.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="risk source not found")
    if payload.feared_event_id is not None:
        feared_event = feared_event_service.get_feared_event(payload.feared_event_id)
        if feared_event is None or feared_event.organization_id != current_user.organization_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="feared event not found")

    risk_origin = service.create_risk_origin(
        CreateRiskOriginCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return RiskOriginRead.model_validate(risk_origin)
