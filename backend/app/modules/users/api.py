from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from backend.app.interfaces.api.dependencies import get_current_user, get_user_service, require_permission
from backend.app.modules.users.schemas import UserCreate, UserRead, UserUpdate
from backend.app.modules.users.service import CreateUserCommand, EmailAlreadyRegisteredError, User, UserService
from backend.app.security.permissions import USERS_MANAGE, USERS_READ

router = APIRouter()


@router.get(
    "",
    response_model=list[UserRead],
    dependencies=[Depends(require_permission(USERS_READ))],
)
def list_users(
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service),
) -> list[UserRead]:
    return [UserRead.model_validate(item) for item in service.list_users(current_user.organization_id)]


@router.post(
    "",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(USERS_MANAGE))],
)
def create_user(
    payload: UserCreate,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service),
) -> UserRead:
    try:
        user = service.create_user(
            CreateUserCommand(
                organization_id=current_user.organization_id,
                email=payload.email,
                full_name=payload.full_name,
                password=payload.password,
                is_superuser=payload.is_superuser,
            )
        )
    except EmailAlreadyRegisteredError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already registered") from exc
    return UserRead.model_validate(user)


@router.get(
    "/{user_id}",
    response_model=UserRead,
    dependencies=[Depends(require_permission(USERS_READ))],
)
def get_user(
    user_id: UUID,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service),
) -> UserRead:
    user = service.get_user(user_id)
    if user is None or user.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    return UserRead.model_validate(user)


@router.patch(
    "/{user_id}",
    response_model=UserRead,
    dependencies=[Depends(require_permission(USERS_MANAGE))],
)
def update_user(
    user_id: UUID,
    payload: UserUpdate,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service),
) -> UserRead:
    target = service.get_user(user_id)
    if target is None or target.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    user = service.update_profile(user_id, payload.full_name, payload.is_active)
    return UserRead.model_validate(user)


@router.post(
    "/{user_id}/roles/{role_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_permission(USERS_MANAGE))],
)
def assign_role(
    user_id: UUID,
    role_id: UUID,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service),
) -> None:
    target = service.get_user(user_id)
    if target is None or target.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    service.assign_role(user_id, role_id)


@router.delete(
    "/{user_id}/roles/{role_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_permission(USERS_MANAGE))],
)
def remove_role(
    user_id: UUID,
    role_id: UUID,
    current_user: User = Depends(get_current_user),
    service: UserService = Depends(get_user_service),
) -> None:
    target = service.get_user(user_id)
    if target is None or target.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    service.remove_role(user_id, role_id)
