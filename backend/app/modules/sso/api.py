from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_sso_service,
    require_permission,
)
from backend.app.modules.sso.schemas import SsoConnectionRead, SsoConnectionUpdate
from backend.app.modules.sso.service import ConfigureSsoCommand, SsoService
from backend.app.modules.users.service import User
from backend.app.security.permissions import SSO_MANAGE
from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.get(
    "/connection",
    response_model=SsoConnectionRead | None,
    dependencies=[Depends(require_permission(SSO_MANAGE))],
)
def get_connection(
    current_user: User = Depends(get_current_user),
    service: SsoService = Depends(get_sso_service),
) -> SsoConnectionRead | None:
    connection = service.get_connection(current_user.organization_id)
    return SsoConnectionRead.model_validate(connection) if connection else None


@router.put(
    "/connection",
    response_model=SsoConnectionRead,
    dependencies=[Depends(require_permission(SSO_MANAGE))],
)
def configure_connection(
    payload: SsoConnectionUpdate,
    current_user: User = Depends(get_current_user),
    service: SsoService = Depends(get_sso_service),
) -> SsoConnectionRead:
    connection = service.configure(
        ConfigureSsoCommand(
            organization_id=current_user.organization_id,
            actor_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return SsoConnectionRead.model_validate(connection)


@router.delete(
    "/connection",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_permission(SSO_MANAGE))],
)
def delete_connection(
    current_user: User = Depends(get_current_user),
    service: SsoService = Depends(get_sso_service),
) -> None:
    service.remove(current_user.organization_id)
