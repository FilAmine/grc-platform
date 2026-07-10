import secrets
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol
from uuid import UUID

from backend.app.modules.organizations.service import CreateOrganizationCommand, OrganizationService
from backend.app.modules.roles.service import RoleService
from backend.app.modules.sso.oidc_client import OidcClient, OidcError
from backend.app.modules.sso.service import SsoService
from backend.app.modules.users.service import (
    AccountLockedError,
    CreateUserCommand,
    User,
    UserService,
)
from backend.app.security.tokens import (
    InvalidTokenError,
    create_access_token,
    create_sso_state_token,
    decode_sso_state_token,
    generate_refresh_token,
    hash_refresh_token,
    refresh_token_expiry,
)


@dataclass(frozen=True)
class TokenPair:
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


@dataclass(frozen=True)
class RegisterOrganizationCommand:
    organization_name: str
    organization_slug: str
    admin_email: str
    admin_full_name: str
    admin_password: str


class InvalidCredentialsError(Exception):
    pass


class InvalidRefreshTokenError(Exception):
    pass


class SsoNotConfiguredError(Exception):
    """No SSO connection exists for the organization, it's disabled, or the
    organization itself doesn't exist -- deliberately one error type for all
    three so the API layer can map them to a single 404 without leaking
    which case it was (same reasoning as the users module's cross-tenant
    404-not-403 pattern)."""


class InvalidSsoStateError(Exception):
    pass


class SsoLoginError(Exception):
    pass


class RefreshTokenSink(Protocol):
    def create(self, user_id: UUID, token_hash: str, expires_at: datetime) -> None: ...

    def get_active_by_hash(self, token_hash: str, now: datetime) -> object | None: ...

    def revoke(self, token_id: UUID, now: datetime) -> None:
        ...

    def revoke_all_for_user(self, user_id: UUID, now: datetime) -> None:
        ...


ADMIN_ROLE_NAME = "Admin"


class AuthService:
    def __init__(
        self,
        organizations: OrganizationService,
        users: UserService,
        roles: RoleService,
        refresh_tokens: RefreshTokenSink,
        sso: SsoService,
        oidc_client: OidcClient,
    ) -> None:
        self._organizations = organizations
        self._users = users
        self._roles = roles
        self._refresh_tokens = refresh_tokens
        self._sso = sso
        self._oidc_client = oidc_client

    def register_organization(self, command: RegisterOrganizationCommand) -> tuple[User, TokenPair]:
        organization = self._organizations.create_organization(
            CreateOrganizationCommand(name=command.organization_name, slug=command.organization_slug)
        )
        admin = self._users.create_user(
            CreateUserCommand(
                organization_id=organization.id,
                email=command.admin_email,
                full_name=command.admin_full_name,
                password=command.admin_password,
                is_superuser=False,
            )
        )
        admin_role = next(
            (role for role in self._roles.list_roles(organization.id) if role.name == ADMIN_ROLE_NAME),
            None,
        )
        if admin_role is not None:
            self._users.assign_role(admin.id, admin_role.id)
        return admin, self.issue_tokens(admin)

    def login(self, email: str, password: str) -> TokenPair:
        try:
            user = self._users.verify_credentials(email, password, datetime.now(UTC))
        except AccountLockedError as exc:
            raise InvalidCredentialsError(str(exc)) from exc
        return self.issue_tokens(user)

    def refresh(self, refresh_token: str) -> TokenPair:
        now = datetime.now(UTC)
        token_hash = hash_refresh_token(refresh_token)
        stored = self._refresh_tokens.get_active_by_hash(token_hash, now)
        if stored is None:
            raise InvalidRefreshTokenError("refresh token invalid or expired")
        user = self._users.get_user(stored.user_id)
        if user is None or not user.is_active:
            raise InvalidRefreshTokenError("account no longer active")
        self._refresh_tokens.revoke(stored.id, now)
        return self.issue_tokens(user)

    def logout(self, refresh_token: str) -> None:
        now = datetime.now(UTC)
        token_hash = hash_refresh_token(refresh_token)
        stored = self._refresh_tokens.get_active_by_hash(token_hash, now)
        if stored is not None:
            self._refresh_tokens.revoke(stored.id, now)

    def build_sso_authorization_url(self, organization_slug: str, redirect_uri: str) -> str:
        organization = self._organizations.get_organization_by_slug(organization_slug)
        if organization is None:
            raise SsoNotConfiguredError(f"no organization with slug {organization_slug!r}")
        connection = self._sso.get_connection(organization.id)
        if connection is None or not connection.is_enabled:
            raise SsoNotConfiguredError(f"SSO is not configured for organization {organization_slug!r}")
        state = create_sso_state_token(str(organization.id))
        try:
            return self._oidc_client.build_authorization_url(
                connection.issuer, connection.client_id, redirect_uri, state
            )
        except OidcError as exc:
            raise SsoLoginError(str(exc)) from exc

    def complete_sso_login(self, state: str, code: str, redirect_uri: str) -> TokenPair:
        try:
            organization_id = UUID(decode_sso_state_token(state))
        except (InvalidTokenError, ValueError) as exc:
            raise InvalidSsoStateError(str(exc)) from exc

        connection = self._sso.get_connection(organization_id)
        if connection is None or not connection.is_enabled:
            raise SsoNotConfiguredError(f"SSO is not configured for organization {organization_id}")

        try:
            claims = self._oidc_client.exchange_code(
                connection.issuer, connection.client_id, connection.client_secret, redirect_uri, code
            )
        except OidcError as exc:
            raise SsoLoginError(str(exc)) from exc

        user = self._users.get_by_email(claims.email)
        if user is None:
            user = self._users.create_user(
                CreateUserCommand(
                    organization_id=organization_id,
                    email=claims.email,
                    full_name=claims.name or claims.email.split("@")[0],
                    # Random, never-communicated password: this user can only
                    # ever authenticate via SSO, never the password-login form.
                    password=secrets.token_urlsafe(32),
                )
            )
            if connection.default_role_id is not None:
                self._users.assign_role(user.id, connection.default_role_id)
        elif user.organization_id != organization_id:
            # Emails are globally unique across the whole platform (see
            # users.email's unique constraint), not per-org, so this is a
            # real, reachable case: the email this IdP vouched for already
            # belongs to a *different* tenant's account. Fail closed rather
            # than issue tokens for the wrong organization.
            raise SsoLoginError("account email belongs to a different organization")

        return self.issue_tokens(user)

    def issue_tokens(self, user: User) -> TokenPair:
        access_token = create_access_token(str(user.id), str(user.organization_id))
        refresh_token = generate_refresh_token()
        self._refresh_tokens.create(
            user.id, hash_refresh_token(refresh_token), refresh_token_expiry()
        )
        return TokenPair(access_token=access_token, refresh_token=refresh_token)
