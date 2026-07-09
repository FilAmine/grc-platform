from backend.app.interfaces.api.dependencies import get_permission_service, require_permission
from backend.app.modules.permissions.schemas import PermissionRead
from backend.app.modules.permissions.service import PermissionService
from backend.app.security.permissions import ROLES_MANAGE
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get(
    "",
    response_model=list[PermissionRead],
    dependencies=[Depends(require_permission(ROLES_MANAGE))],
)
def list_permissions(
    service: PermissionService = Depends(get_permission_service),
) -> list[PermissionRead]:
    return [PermissionRead.model_validate(item) for item in service.list_permissions()]
