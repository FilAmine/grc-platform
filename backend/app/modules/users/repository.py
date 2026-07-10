from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from backend.app.modules.permissions.models import PermissionModel
from backend.app.modules.roles.models import RoleModel, role_permissions
from backend.app.modules.users.models import UserModel, user_roles
from backend.app.modules.users.service import User
from sqlalchemy import exists, select
from sqlalchemy.orm import Session


def to_user(model: UserModel) -> User:
    return User(
        id=model.id,
        organization_id=model.organization_id,
        email=model.email,
        hashed_password=model.hashed_password,
        full_name=model.full_name,
        is_active=model.is_active,
        is_superuser=model.is_superuser,
        failed_login_attempts=model.failed_login_attempts,
        locked_until=model.locked_until,
        role_ids=[role.id for role in model.roles],
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class UserRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def create(
        self, organization_id: UUID, email: str, full_name: str, hashed_password: str, is_superuser: bool
    ) -> User:
        raise NotImplementedError

    @abstractmethod
    def update_profile(self, user_id: UUID, full_name: str | None, is_active: bool | None) -> User:
        raise NotImplementedError

    @abstractmethod
    def record_login_success(self, user_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def record_login_failure(self, user_id: UUID, locked_until: datetime | None) -> None:
        raise NotImplementedError

    @abstractmethod
    def assign_role(self, user_id: UUID, role_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_role(self, user_id: UUID, role_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def has_permission(self, user_id: UUID, permission_code: str) -> bool:
        raise NotImplementedError


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[User]:
        statement = (
            select(UserModel)
            .where(UserModel.organization_id == organization_id, UserModel.deleted_at.is_(None))
            .order_by(UserModel.email)
        )
        rows = self._session.scalars(statement).all()
        return [to_user(row) for row in rows]

    def get_by_id(self, user_id: UUID) -> User | None:
        model = self._session.get(UserModel, user_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_user(model)

    def get_by_email(self, email: str) -> User | None:
        statement = select(UserModel).where(
            UserModel.email == email, UserModel.deleted_at.is_(None)
        )
        model = self._session.scalars(statement).first()
        return to_user(model) if model else None

    def create(
        self, organization_id: UUID, email: str, full_name: str, hashed_password: str, is_superuser: bool
    ) -> User:
        model = UserModel(
            organization_id=organization_id,
            email=email,
            full_name=full_name,
            hashed_password=hashed_password,
            is_superuser=is_superuser,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_user(model)

    def update_profile(self, user_id: UUID, full_name: str | None, is_active: bool | None) -> User:
        model = self._session.get(UserModel, user_id)
        if model is None:
            raise ValueError("user not found")
        if full_name is not None:
            model.full_name = full_name
        if is_active is not None:
            model.is_active = is_active
        self._session.commit()
        self._session.refresh(model)
        return to_user(model)

    def record_login_success(self, user_id: UUID) -> None:
        model = self._session.get(UserModel, user_id)
        if model is None:
            return
        model.failed_login_attempts = 0
        model.locked_until = None
        self._session.commit()

    def record_login_failure(self, user_id: UUID, locked_until: datetime | None) -> None:
        model = self._session.get(UserModel, user_id)
        if model is None:
            return
        model.failed_login_attempts += 1
        if locked_until is not None:
            model.locked_until = locked_until
        self._session.commit()

    def assign_role(self, user_id: UUID, role_id: UUID) -> None:
        user = self._session.get(UserModel, user_id)
        role = self._session.get(RoleModel, role_id)
        if user is None or role is None:
            raise ValueError("user or role not found")
        if role not in user.roles:
            user.roles.append(role)
            self._session.commit()

    def remove_role(self, user_id: UUID, role_id: UUID) -> None:
        user = self._session.get(UserModel, user_id)
        if user is None:
            raise ValueError("user not found")
        user.roles = [role for role in user.roles if role.id != role_id]
        self._session.commit()

    def has_permission(self, user_id: UUID, permission_code: str) -> bool:
        statement = select(
            exists().where(
                user_roles.c.user_id == user_id,
                user_roles.c.role_id == role_permissions.c.role_id,
                role_permissions.c.permission_id == PermissionModel.id,
                PermissionModel.code == permission_code,
            )
        )
        return bool(self._session.scalar(statement))
