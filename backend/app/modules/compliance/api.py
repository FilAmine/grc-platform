from fastapi import APIRouter, Depends

from backend.app.interfaces.api.dependencies import get_compliance_service
from backend.app.modules.compliance.schemas import ComplianceSummary
from backend.app.modules.compliance.service import ComplianceService

router = APIRouter()


@router.get("/summary", response_model=ComplianceSummary)
def compliance_summary(
    service: ComplianceService = Depends(get_compliance_service),
) -> ComplianceSummary:
    return ComplianceSummary.model_validate(service.summary())
