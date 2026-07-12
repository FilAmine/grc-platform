from backend.app.interfaces.api.dependencies import get_current_user, get_tenant_service
from backend.app.modules.tenants.schemas import TenantCreate, TenantRead
from backend.app.modules.tenants.service import CreateTenantCommand, TenantService
from backend.app.modules.users.service import User
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get("", response_model=list[TenantRead])
def list_tenants(
    current_user: User = Depends(get_current_user),
    service: TenantService = Depends(get_tenant_service),
) -> list[TenantRead]:
    # Raw is_superuser gate, not require_permission -- matches
    # organizations/api.py exactly. require_permission would let an org-scoped
    # role holding a hypothetical "tenants:read" code through, making a
    # platform-level, cross-org capability delegable to a per-org role, which
    # must never be possible. No permission codes exist for this resource.
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only platform superusers can view tenants",
        )
    return [TenantRead.model_validate(item) for item in service.list_tenants()]


@router.post("", response_model=TenantRead, status_code=status.HTTP_201_CREATED)
def create_tenant(
    payload: TenantCreate,
    current_user: User = Depends(get_current_user),
    service: TenantService = Depends(get_tenant_service),
) -> TenantRead:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only platform superusers can create tenants",
        )
    tenant = service.create_tenant(CreateTenantCommand(**payload.model_dump()))
    return TenantRead.model_validate(tenant)
