from dataclasses import dataclass
from uuid import UUID

from backend.app.modules.compliance.repository import ControlReader, OrganizationReader, RiskReader
from backend.app.modules.controls.service import ControlStatus
from backend.app.modules.risks.service import RiskStatus


@dataclass(frozen=True)
class ComplianceMetric:
    key: str
    value: int | str


class ComplianceService:
    def __init__(
        self,
        organizations: OrganizationReader,
        risks: RiskReader,
        controls: ControlReader,
    ) -> None:
        self._organizations = organizations
        self._risks = risks
        self._controls = controls

    def summary(self, organization_id: UUID) -> dict[str, int | str]:
        risk_items = self._risks.list_risks(organization_id)
        control_items = self._controls.list_controls(organization_id)
        open_risks = len([risk for risk in risk_items if risk.status != RiskStatus.CLOSED])
        active_controls = len(
            [control for control in control_items if control.status == ControlStatus.ACTIVE]
        )
        return {
            "organizations": 1,
            "risks_open": open_risks,
            "controls_active": active_controls,
            "posture": "attention_required" if open_risks else "healthy",
        }
