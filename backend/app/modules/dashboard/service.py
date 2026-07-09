from uuid import UUID

from backend.app.modules.compliance.service import ComplianceService


class DashboardService:
    def __init__(self, compliance: ComplianceService) -> None:
        self._compliance = compliance

    def summary(self, organization_id: UUID) -> dict[str, int | str]:
        return self._compliance.summary(organization_id)
