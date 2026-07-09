from uuid import UUID

from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_role_service,
    require_permission,
)
from backend.app.modules.roles.schemas import RoleCreate, RolePermissionsUpdate, RoleRead
from backend.app.modules.roles.service import CreateRoleCommand, RoleNotEditableError, RoleService
from backend.app.modules.users.service import User
from backend.app.security.permissions import ROLES_MANAGE
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get("", response_model=list[RoleRead])
def list_roles(
    current_user: User = Depends(get_current_user),
    service: RoleService = Depends(get_role_service),
) -> list[RoleRead]:
    return [RoleRead.model_validate(item) for item in service.list_roles(current_user.organization_id)]


@router.post(
    "",
    response_model=RoleRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(ROLES_MANAGE))],
)
def create_role(
    payload: RoleCreate,
    current_user: User = Depends(get_current_user),
    service: RoleService = Depends(get_role_service),
) -> RoleRead:
    role = service.create_role(
        CreateRoleCommand(
            organization_id=current_user.organization_id,
            name=payload.name,
            description=payload.description,
            permission_codes=tuple(payload.permission_codes),
        )
    )
    return RoleRead.model_validate(role)


@router.put(
    "/{role_id}/permissions",
    response_model=RoleRead,
    dependencies=[Depends(require_permission(ROLES_MANAGE))],
)
def set_role_permissions(
    role_id: UUID,
    payload: RolePermissionsUpdate,
    service: RoleService = Depends(get_role_service),
) -> RoleRead:
    try:
        role = service.set_role_permissions(role_id, tuple(payload.permission_codes))
    except RoleNotEditableError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    return RoleRead.model_validate(role)
