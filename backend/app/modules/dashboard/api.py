from fastapi import APIRouter, Depends

from backend.app.interfaces.api.dependencies import get_dashboard_service
from backend.app.modules.dashboard.schemas import ComplianceSummary
from backend.app.modules.dashboard.service import DashboardService

router = APIRouter()


@router.get("/summary", response_model=ComplianceSummary)
def dashboard_summary(
    service: DashboardService = Depends(get_dashboard_service),
) -> ComplianceSummary:
    return ComplianceSummary.model_validate(service.summary())
