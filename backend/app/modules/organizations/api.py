from fastapi import APIRouter, Depends, HTTPException, status

from backend.app.interfaces.api.dependencies import get_current_user, get_organization_service
from backend.app.modules.organizations.schemas import OrganizationCreate, OrganizationRead
from backend.app.modules.organizations.service import CreateOrganizationCommand, OrganizationService
from backend.app.modules.users.service import User

router = APIRouter()


@router.get("", response_model=list[OrganizationRead])
def list_organizations(
    current_user: User = Depends(get_current_user),
    service: OrganizationService = Depends(get_organization_service),
) -> list[OrganizationRead]:
    if current_user.is_superuser:
        return [OrganizationRead.model_validate(item) for item in service.list_organizations()]
    own = service.get_organization(current_user.organization_id)
    return [OrganizationRead.model_validate(own)] if own else []


@router.post("", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
def create_organization(
    payload: OrganizationCreate,
    current_user: User = Depends(get_current_user),
    service: OrganizationService = Depends(get_organization_service),
) -> OrganizationRead:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only platform superusers can create organizations directly; use /auth/register-organization",
        )
    organization = service.create_organization(CreateOrganizationCommand(**payload.model_dump()))
    return OrganizationRead.model_validate(organization)
