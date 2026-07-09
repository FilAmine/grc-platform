from fastapi import APIRouter, Depends

from backend.app.interfaces.api.dependencies import get_current_user, get_dashboard_service, require_permission
from backend.app.modules.dashboard.schemas import ComplianceSummary
from backend.app.modules.dashboard.service import DashboardService
from backend.app.modules.users.service import User
from backend.app.security.permissions import COMPLIANCE_READ

router = APIRouter()


@router.get(
    "/summary",
    response_model=ComplianceSummary,
    dependencies=[Depends(require_permission(COMPLIANCE_READ))],
)
def dashboard_summary(
    current_user: User = Depends(get_current_user),
    service: DashboardService = Depends(get_dashboard_service),
) -> ComplianceSummary:
    return ComplianceSummary.model_validate(service.summary(current_user.organization_id))
