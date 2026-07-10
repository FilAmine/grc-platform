from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Protocol
from uuid import UUID

from backend.app.security.tokens import hash_password, verify_password

MAX_FAILED_LOGIN_ATTEMPTS = 5
LOCKOUT_MINUTES = 15


@dataclass(frozen=True)
class User:
    id: UUID
    organization_id: UUID
    email: str
    hashed_password: str
    full_name: str
    is_active: bool
    is_superuser: bool
    failed_login_attempts: int
    locked_until: datetime | None
    role_ids: list[UUID]
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateUserCommand:
    organization_id: UUID
    email: str
    full_name: str
    password: str
    is_superuser: bool = False


class UserStore(Protocol):
    def list(self, organization_id: UUID) -> list[User]:
        raise NotImplementedError

    def get_by_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError

    def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError

    def create(
        self, organization_id: UUID, email: str, full_name: str, hashed_password: str, is_superuser: bool
    ) -> User:
        raise NotImplementedError

    def update_profile(self, user_id: UUID, full_name: str | None, is_active: bool | None) -> User:
        raise NotImplementedError

    def record_login_success(self, user_id: UUID) -> None:
        raise NotImplementedError

    def record_login_failure(self, user_id: UUID, locked_until: datetime | None) -> None:
        raise NotImplementedError

    def assign_role(self, user_id: UUID, role_id: UUID) -> None:
        raise NotImplementedError

    def remove_role(self, user_id: UUID, role_id: UUID) -> None:
        raise NotImplementedError

    def has_permission(self, user_id: UUID, permission_code: str) -> bool:
        raise NotImplementedError


class EmailAlreadyRegisteredError(Exception):
    pass


class AccountLockedError(Exception):
    pass


class UserService:
    def __init__(self, users: UserStore) -> None:
        self._users = users

    def list_users(self, organization_id: UUID) -> list[User]:
        return self._users.list(organization_id)

    def get_user(self, user_id: UUID) -> User | None:
        return self._users.get_by_id(user_id)

    def get_by_email(self, email: str) -> User | None:
        return self._users.get_by_email(email)

    def create_user(self, command: CreateUserCommand) -> User:
        if self._users.get_by_email(command.email) is not None:
            raise EmailAlreadyRegisteredError(command.email)
        return self._users.create(
            organization_id=command.organization_id,
            email=command.email,
            full_name=command.full_name,
            hashed_password=hash_password(command.password),
            is_superuser=command.is_superuser,
        )

    def update_profile(
        self, user_id: UUID, full_name: str | None = None, is_active: bool | None = None
    ) -> User:
        return self._users.update_profile(user_id, full_name, is_active)

    def assign_role(self, user_id: UUID, role_id: UUID) -> None:
        self._users.assign_role(user_id, role_id)

    def remove_role(self, user_id: UUID, role_id: UUID) -> None:
        self._users.remove_role(user_id, role_id)

    def has_permission(self, user_id: UUID, permission_code: str) -> bool:
        return self._users.has_permission(user_id, permission_code)

    def verify_credentials(self, email: str, password: str, now: datetime) -> User:
        user = self._users.get_by_email(email)
        if user is None:
            raise AccountLockedError("invalid credentials")
        locked_until = user.locked_until
        if locked_until is not None:
            if locked_until.tzinfo is None:
                locked_until = locked_until.replace(tzinfo=UTC)
            if locked_until > now:
                raise AccountLockedError("account temporarily locked")
        if not user.is_active or not verify_password(password, user.hashed_password):
            locked_until = None
            if user.failed_login_attempts + 1 >= MAX_FAILED_LOGIN_ATTEMPTS:
                locked_until = now + timedelta(minutes=LOCKOUT_MINUTES)
            self._users.record_login_failure(user.id, locked_until)
            raise AccountLockedError("invalid credentials")
        self._users.record_login_success(user.id)
        return user
