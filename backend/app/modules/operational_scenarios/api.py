from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_operational_scenario_service,
    get_strategic_scenario_service,
    require_permission,
)
from backend.app.modules.operational_scenarios.schemas import (
    OperationalScenarioCreate,
    OperationalScenarioRead,
)
from backend.app.modules.operational_scenarios.service import (
    CreateOperationalScenarioCommand,
    OperationalScenarioService,
)
from backend.app.modules.strategic_scenarios.service import StrategicScenarioService
from backend.app.modules.users.service import User
from backend.app.security.permissions import (
    OPERATIONAL_SCENARIOS_MANAGE,
    OPERATIONAL_SCENARIOS_READ,
)
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "",
    response_model=list[OperationalScenarioRead],
    dependencies=[Depends(require_permission(OPERATIONAL_SCENARIOS_READ))],
)
def list_operational_scenarios(
    current_user: User = Depends(get_current_user),
    service: OperationalScenarioService = Depends(get_operational_scenario_service),
) -> list[OperationalScenarioRead]:
    return [
        OperationalScenarioRead.model_validate(item)
        for item in service.list_operational_scenarios(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=OperationalScenarioRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(OPERATIONAL_SCENARIOS_MANAGE))],
)
def create_operational_scenario(
    payload: OperationalScenarioCreate,
    current_user: User = Depends(get_current_user),
    service: OperationalScenarioService = Depends(get_operational_scenario_service),
    strategic_scenario_service: StrategicScenarioService = Depends(get_strategic_scenario_service),
) -> OperationalScenarioRead:
    strategic_scenario = strategic_scenario_service.get_strategic_scenario(payload.strategic_scenario_id)
    if strategic_scenario is None or strategic_scenario.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="strategic scenario not found")

    operational_scenario = service.create_operational_scenario(
        CreateOperationalScenarioCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return OperationalScenarioRead.model_validate(operational_scenario)
