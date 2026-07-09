from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol
from uuid import UUID

from backend.app.modules.organizations.service import CreateOrganizationCommand, OrganizationService
from backend.app.modules.roles.service import RoleService
from backend.app.modules.users.service import (
    AccountLockedError,
    CreateUserCommand,
    User,
    UserService,
)
from backend.app.security.tokens import (
    create_access_token,
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
    ) -> None:
        self._organizations = organizations
        self._users = users
        self._roles = roles
        self._refresh_tokens = refresh_tokens

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
        return admin, self._issue_tokens(admin)

    def login(self, email: str, password: str) -> TokenPair:
        try:
            user = self._users.verify_credentials(email, password, datetime.now(UTC))
        except AccountLockedError as exc:
            raise InvalidCredentialsError(str(exc)) from exc
        return self._issue_tokens(user)

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
        return self._issue_tokens(user)

    def logout(self, refresh_token: str) -> None:
        now = datetime.now(UTC)
        token_hash = hash_refresh_token(refresh_token)
        stored = self._refresh_tokens.get_active_by_hash(token_hash, now)
        if stored is not None:
            self._refresh_tokens.revoke(stored.id, now)

    def _issue_tokens(self, user: User) -> TokenPair:
        access_token = create_access_token(str(user.id), str(user.organization_id))
        refresh_token = generate_refresh_token()
        self._refresh_tokens.create(
            user.id, hash_refresh_token(refresh_token), refresh_token_expiry()
        )
        return TokenPair(access_token=access_token, refresh_token=refresh_token)
