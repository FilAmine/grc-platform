from fastapi import APIRouter, Depends

from backend.app.application.use_cases import ControlService, OrganizationService, RiskService
from backend.app.domain.entities import ControlStatus, RiskStatus
from backend.app.interfaces.api.dependencies import (
    get_control_service,
    get_organization_service,
    get_risk_service,
)
from backend.app.interfaces.api.v1.schemas import ComplianceSummary

router = APIRouter()


@router.get("/summary", response_model=ComplianceSummary)
def compliance_summary(
    organizations: OrganizationService = Depends(get_organization_service),
    risks: RiskService = Depends(get_risk_service),
    controls: ControlService = Depends(get_control_service),
) -> ComplianceSummary:
    risk_items = risks.list_risks()
    control_items = controls.list_controls()
    open_risks = len([risk for risk in risk_items if risk.status != RiskStatus.CLOSED])
    active_controls = len([control for control in control_items if control.status == ControlStatus.ACTIVE])
    posture = "attention_required" if open_risks else "healthy"
    return ComplianceSummary(
        organizations=len(organizations.list_organizations()),
        risks_open=open_risks,
        controls_active=active_controls,
        posture=posture,
    )
