from urllib.parse import quote

from backend.app.core.config import settings
from backend.app.core.rate_limit import rate_limit
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
    InvalidSsoStateError,
    RegisterOrganizationCommand,
    SsoLoginError,
    SsoNotConfiguredError,
)
from backend.app.modules.users.schemas import UserRead
from backend.app.modules.users.service import EmailAlreadyRegisteredError, User
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

# Thresholds live here, next to the routes they gate, rather than as Settings
# fields -- same "hardcoded constant, not per-deployment-configurable" choice
# already made for MAX_FAILED_LOGIN_ATTEMPTS/LOCKOUT_MINUTES in
# modules/users/service.py.
LOGIN_RATE_LIMIT = (10, 60)
REGISTER_ORGANIZATION_RATE_LIMIT = (5, 3600)
REFRESH_RATE_LIMIT = (30, 60)  # higher: legitimate 401-triggered auto-refresh
SSO_LOGIN_RATE_LIMIT = (20, 60)
SSO_CALLBACK_RATE_LIMIT = (20, 60)


def _sso_redirect_uri() -> str:
    return f"{settings.backend_base_url}{settings.api_v1_prefix}/auth/sso/callback"


@router.post(
    "/register-organization",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(rate_limit("register-organization", *REGISTER_ORGANIZATION_RATE_LIMIT))],
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


@router.post(
    "/login", response_model=TokenResponse, dependencies=[Depends(rate_limit("login", *LOGIN_RATE_LIMIT))]
)
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


@router.post(
    "/refresh",
    response_model=TokenResponse,
    dependencies=[Depends(rate_limit("refresh", *REFRESH_RATE_LIMIT))],
)
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


@router.get(
    "/sso/{organization_slug}/login",
    dependencies=[Depends(rate_limit("sso-login", *SSO_LOGIN_RATE_LIMIT))],
)
def sso_login(
    organization_slug: str,
    service: AuthService = Depends(get_auth_service),
) -> RedirectResponse:
    try:
        authorization_url = service.build_sso_authorization_url(organization_slug, _sso_redirect_uri())
    except SsoNotConfiguredError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="SSO is not configured for this organization"
        ) from exc
    except SsoLoginError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY, detail=f"could not reach the identity provider: {exc}"
        ) from exc
    return RedirectResponse(authorization_url, status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@router.get(
    "/sso/callback",
    dependencies=[Depends(rate_limit("sso-callback", *SSO_CALLBACK_RATE_LIMIT))],
)
def sso_callback(
    code: str,
    state: str,
    service: AuthService = Depends(get_auth_service),
) -> RedirectResponse:
    try:
        tokens = service.complete_sso_login(state, code, _sso_redirect_uri())
    except (InvalidSsoStateError, SsoNotConfiguredError, SsoLoginError) as exc:
        target = f"{settings.frontend_base_url}/sso/callback#error={quote(str(exc))}"
        return RedirectResponse(target, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    target = (
        f"{settings.frontend_base_url}/sso/callback"
        f"#access_token={tokens.access_token}&refresh_token={tokens.refresh_token}"
    )
    return RedirectResponse(target, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
