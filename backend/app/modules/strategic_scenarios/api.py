from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_ecosystem_party_service,
    get_feared_event_service,
    get_risk_origin_service,
    get_strategic_scenario_service,
    require_permission,
)
from backend.app.modules.ecosystem_parties.service import EcosystemPartyService
from backend.app.modules.feared_events.service import FearedEventService
from backend.app.modules.risk_origins.service import RiskOriginService
from backend.app.modules.strategic_scenarios.schemas import StrategicScenarioCreate, StrategicScenarioRead
from backend.app.modules.strategic_scenarios.service import (
    CreateStrategicScenarioCommand,
    StrategicScenarioService,
)
from backend.app.modules.users.service import User
from backend.app.security.permissions import STRATEGIC_SCENARIOS_MANAGE, STRATEGIC_SCENARIOS_READ
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "",
    response_model=list[StrategicScenarioRead],
    dependencies=[Depends(require_permission(STRATEGIC_SCENARIOS_READ))],
)
def list_strategic_scenarios(
    current_user: User = Depends(get_current_user),
    service: StrategicScenarioService = Depends(get_strategic_scenario_service),
) -> list[StrategicScenarioRead]:
    return [
        StrategicScenarioRead.model_validate(item)
        for item in service.list_strategic_scenarios(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=StrategicScenarioRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(STRATEGIC_SCENARIOS_MANAGE))],
)
def create_strategic_scenario(
    payload: StrategicScenarioCreate,
    current_user: User = Depends(get_current_user),
    service: StrategicScenarioService = Depends(get_strategic_scenario_service),
    risk_origin_service: RiskOriginService = Depends(get_risk_origin_service),
    feared_event_service: FearedEventService = Depends(get_feared_event_service),
    ecosystem_party_service: EcosystemPartyService = Depends(get_ecosystem_party_service),
) -> StrategicScenarioRead:
    # Same cross-tenant validation pattern as risk_origins/api.py.
    risk_origin = risk_origin_service.get_risk_origin(payload.risk_origin_id)
    if risk_origin is None or risk_origin.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="risk origin not found")
    # Methodological check, not just structural: EBIOS RM Workshop 3 scenarios
    # elaborate the SR/OV pairs Workshop 2 prioritized ("retained") -- building
    # one from a pair that was explicitly not retained skips that prioritization
    # step rather than just being an unusual-but-valid case.
    if not risk_origin.retained:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="risk origin is not retained -- mark it retained before building a strategic scenario from it",
        )

    feared_event = feared_event_service.get_feared_event(payload.feared_event_id)
    if feared_event is None or feared_event.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="feared event not found")

    if payload.ecosystem_party_id is not None:
        ecosystem_party = ecosystem_party_service.get_ecosystem_party(payload.ecosystem_party_id)
        if ecosystem_party is None or ecosystem_party.organization_id != current_user.organization_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ecosystem party not found")

    strategic_scenario = service.create_strategic_scenario(
        CreateStrategicScenarioCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return StrategicScenarioRead.model_validate(strategic_scenario)
