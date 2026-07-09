from backend.app.interfaces.api.dependencies import get_auth_service, get_current_user
from backend.app.modules.auth.schemas import (
    RefreshRequest,
    RegisterOrganizationRequest,
    TokenResponse,
)
from backend.app.modules.auth.service import (
    AuthService,
    InvalidCredentialsError,
    InvalidRefreshTokenError,
    RegisterOrganizationCommand,
)
from backend.app.modules.users.schemas import UserRead
from backend.app.modules.users.service import EmailAlreadyRegisteredError, User
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post(
    "/register-organization", response_model=TokenResponse, status_code=status.HTTP_201_CREATED
)
def register_organization(
    payload: RegisterOrganizationRequest,
    service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    try:
        _, tokens = service.register_organization(
            RegisterOrganizationCommand(
                organization_name=payload.organization_name,
                organization_slug=payload.organization_slug,
                admin_email=payload.admin_email,
                admin_full_name=payload.admin_full_name,
                admin_password=payload.admin_password,
            )
        )
    except EmailAlreadyRegisteredError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already registered") from exc
    return TokenResponse(access_token=tokens.access_token, refresh_token=tokens.refresh_token)


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    try:
        tokens = service.login(form_data.username, form_data.password)
    except InvalidCredentialsError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials"
        ) from exc
    return TokenResponse(access_token=tokens.access_token, refresh_token=tokens.refresh_token)


@router.post("/refresh", response_model=TokenResponse)
def refresh(
    payload: RefreshRequest,
    service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    try:
        tokens = service.refresh(payload.refresh_token)
    except InvalidRefreshTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid refresh token"
        ) from exc
    return TokenResponse(access_token=tokens.access_token, refresh_token=tokens.refresh_token)


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    payload: RefreshRequest,
    service: AuthService = Depends(get_auth_service),
) -> None:
    service.logout(payload.refresh_token)


@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user)) -> UserRead:
    return UserRead.model_validate(current_user)
