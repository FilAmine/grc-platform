from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_risk_treatment_service,
    get_strategic_scenario_service,
    require_permission,
)
from backend.app.modules.risk_treatments.schemas import RiskTreatmentCreate, RiskTreatmentRead
from backend.app.modules.risk_treatments.service import CreateRiskTreatmentCommand, RiskTreatmentService
from backend.app.modules.strategic_scenarios.service import StrategicScenarioService
from backend.app.modules.users.service import User
from backend.app.security.permissions import RISK_TREATMENTS_MANAGE, RISK_TREATMENTS_READ
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "",
    response_model=list[RiskTreatmentRead],
    dependencies=[Depends(require_permission(RISK_TREATMENTS_READ))],
)
def list_risk_treatments(
    current_user: User = Depends(get_current_user),
    service: RiskTreatmentService = Depends(get_risk_treatment_service),
) -> list[RiskTreatmentRead]:
    return [
        RiskTreatmentRead.model_validate(item)
        for item in service.list_risk_treatments(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=RiskTreatmentRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(RISK_TREATMENTS_MANAGE))],
)
def create_risk_treatment(
    payload: RiskTreatmentCreate,
    current_user: User = Depends(get_current_user),
    service: RiskTreatmentService = Depends(get_risk_treatment_service),
    strategic_scenario_service: StrategicScenarioService = Depends(get_strategic_scenario_service),
) -> RiskTreatmentRead:
    strategic_scenario = strategic_scenario_service.get_strategic_scenario(payload.strategic_scenario_id)
    if strategic_scenario is None or strategic_scenario.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="strategic scenario not found")

    risk_treatment = service.create_risk_treatment(
        CreateRiskTreatmentCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return RiskTreatmentRead.model_validate(risk_treatment)
