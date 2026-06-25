from fastapi import APIRouter, Depends, status

from backend.app.application.use_cases import CreateOrganizationCommand, OrganizationService
from backend.app.interfaces.api.dependencies import get_organization_service
from backend.app.interfaces.api.v1.schemas import OrganizationCreate, OrganizationRead

router = APIRouter()


@router.get("", response_model=list[OrganizationRead])
def list_organizations(
    service: OrganizationService = Depends(get_organization_service),
) -> list[OrganizationRead]:
    return [OrganizationRead.model_validate(item) for item in service.list_organizations()]


@router.post("", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
def create_organization(
    payload: OrganizationCreate,
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationRead:
    organization = service.create_organization(CreateOrganizationCommand(**payload.model_dump()))
    return OrganizationRead.model_validate(organization)
