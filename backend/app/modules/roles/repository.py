from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from backend.app.modules.permissions.models import PermissionModel
from backend.app.modules.roles.models import RoleModel
from backend.app.modules.roles.service import Role


def to_role(model: RoleModel) -> Role:
    return Role(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        is_system=model.is_system,
        permission_codes=tuple(sorted(p.code for p in model.permissions)),
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class RoleRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID) -> list[Role]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, role_id: UUID) -> Role | None:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        permission_codes: tuple[str, ...],
    ) -> Role:
        raise NotImplementedError

    @abstractmethod
    def set_permissions(self, role_id: UUID, permission_codes: tuple[str, ...]) -> Role:
        raise NotImplementedError


class SqlAlchemyRoleRepository(RoleRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Role]:
        statement = select(RoleModel).where(
            or_(RoleModel.organization_id == organization_id, RoleModel.organization_id.is_(None))
        ).order_by(RoleModel.name)
        rows = self._session.scalars(statement).unique().all()
        return [to_role(row) for row in rows]

    def get_by_id(self, role_id: UUID) -> Role | None:
        model = self._session.get(RoleModel, role_id)
        return to_role(model) if model else None

    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        permission_codes: tuple[str, ...],
    ) -> Role:
        permissions = self._permissions_by_code(permission_codes)
        model = RoleModel(
            organization_id=organization_id,
            name=name,
            description=description,
            is_system=False,
            permissions=permissions,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_role(model)

    def set_permissions(self, role_id: UUID, permission_codes: tuple[str, ...]) -> Role:
        model = self._session.get(RoleModel, role_id)
        if model is None:
            raise ValueError("role not found")
        model.permissions = self._permissions_by_code(permission_codes)
        self._session.commit()
        self._session.refresh(model)
        return to_role(model)

    def _permissions_by_code(self, codes: tuple[str, ...]) -> list[PermissionModel]:
        if not codes:
            return []
        rows = self._session.scalars(
            select(PermissionModel).where(PermissionModel.code.in_(codes))
        ).all()
        return list(rows)
