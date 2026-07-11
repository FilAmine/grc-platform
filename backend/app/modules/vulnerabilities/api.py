from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_vulnerability_service,
    require_permission,
)
from backend.app.modules.users.service import User
from backend.app.modules.vulnerabilities.schemas import VulnerabilityCreate, VulnerabilityRead
from backend.app.modules.vulnerabilities.service import CreateVulnerabilityCommand, VulnerabilityService
from backend.app.security.permissions import VULNERABILITIES_MANAGE, VULNERABILITIES_READ
from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.get(
    "",
    response_model=list[VulnerabilityRead],
    dependencies=[Depends(require_permission(VULNERABILITIES_READ))],
)
def list_vulnerabilities(
    current_user: User = Depends(get_current_user),
    service: VulnerabilityService = Depends(get_vulnerability_service),
) -> list[VulnerabilityRead]:
    return [
        VulnerabilityRead.model_validate(item)
        for item in service.list_vulnerabilities(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=VulnerabilityRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(VULNERABILITIES_MANAGE))],
)
def create_vulnerability(
    payload: VulnerabilityCreate,
    current_user: User = Depends(get_current_user),
    service: VulnerabilityService = Depends(get_vulnerability_service),
) -> VulnerabilityRead:
    vulnerability = service.create_vulnerability(
        CreateVulnerabilityCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return VulnerabilityRead.model_validate(vulnerability)
