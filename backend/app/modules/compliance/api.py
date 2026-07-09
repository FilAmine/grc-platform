from fastapi import APIRouter, Depends

from backend.app.interfaces.api.dependencies import get_compliance_service, get_current_user, require_permission
from backend.app.modules.compliance.schemas import ComplianceSummary
from backend.app.modules.compliance.service import ComplianceService
from backend.app.modules.users.service import User
from backend.app.security.permissions import COMPLIANCE_READ

router = APIRouter()


@router.get(
    "/summary",
    response_model=ComplianceSummary,
    dependencies=[Depends(require_permission(COMPLIANCE_READ))],
)
def compliance_summary(
    current_user: User = Depends(get_current_user),
    service: ComplianceService = Depends(get_compliance_service),
) -> ComplianceSummary:
    return ComplianceSummary.model_validate(service.summary(current_user.organization_id))
