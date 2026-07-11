from backend.app.interfaces.api.dependencies import (
    get_asset_service,
    get_current_user,
    get_feared_event_service,
    get_risk_service,
    get_threat_service,
    get_vulnerability_service,
    require_permission,
)
from backend.app.modules.assets.service import AssetService
from backend.app.modules.feared_events.service import FearedEventService
from backend.app.modules.risks.schemas import RiskCreate, RiskRead
from backend.app.modules.risks.service import CreateRiskCommand, RiskService
from backend.app.modules.threats.service import ThreatService
from backend.app.modules.users.service import User
from backend.app.modules.vulnerabilities.service import VulnerabilityService
from backend.app.security.permissions import RISKS_MANAGE, RISKS_READ
from fastapi import APIRouter, Depends, HTTPException, status

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
    asset_service: AssetService = Depends(get_asset_service),
    threat_service: ThreatService = Depends(get_threat_service),
    vulnerability_service: VulnerabilityService = Depends(get_vulnerability_service),
    feared_event_service: FearedEventService = Depends(get_feared_event_service),
) -> RiskRead:
    # Each optional FK only proves "some row exists," not "same tenant" --
    # same cross-tenant validation pattern as departments/api.py's
    # parent_department_id check, repeated once per new link.
    if payload.asset_id is not None:
        asset = asset_service.get_asset(payload.asset_id)
        if asset is None or asset.organization_id != current_user.organization_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="asset not found")
    if payload.threat_id is not None:
        threat = threat_service.get_threat(payload.threat_id)
        if threat is None or threat.organization_id != current_user.organization_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="threat not found")
    if payload.vulnerability_id is not None:
        vulnerability = vulnerability_service.get_vulnerability(payload.vulnerability_id)
        if vulnerability is None or vulnerability.organization_id != current_user.organization_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vulnerability not found")
    if payload.feared_event_id is not None:
        feared_event = feared_event_service.get_feared_event(payload.feared_event_id)
        if feared_event is None or feared_event.organization_id != current_user.organization_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="feared event not found")

    risk = service.create_risk(
        CreateRiskCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return RiskRead.model_validate(risk)
