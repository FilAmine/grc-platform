from uuid import UUID

from fastapi import APIRouter, Depends, Query, status

from backend.app.application.use_cases import CreateRiskCommand, RiskService
from backend.app.interfaces.api.dependencies import get_risk_service
from backend.app.interfaces.api.v1.schemas import RiskCreate, RiskRead

router = APIRouter()


@router.get("", response_model=list[RiskRead])
def list_risks(
    organization_id: UUID | None = Query(default=None),
    service: RiskService = Depends(get_risk_service),
) -> list[RiskRead]:
    return [RiskRead.model_validate(item) for item in service.list_risks(organization_id)]


@router.post("", response_model=RiskRead, status_code=status.HTTP_201_CREATED)
def create_risk(
    payload: RiskCreate,
    service: RiskService = Depends(get_risk_service),
) -> RiskRead:
    risk = service.create_risk(CreateRiskCommand(**payload.model_dump()))
    return RiskRead.model_validate(risk)
