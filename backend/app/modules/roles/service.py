from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class Role:
    id: UUID
    organization_id: UUID | None
    name: str
    description: str
    is_system: bool
    permission_codes: tuple[str, ...]
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateRoleCommand:
    organization_id: UUID
    name: str
    description: str
    permission_codes: tuple[str, ...] = ()


class RoleNotEditableError(Exception):
    """Raised when attempting to modify a system role's permissions."""


class RoleStore(Protocol):
    def list(self, organization_id: UUID) -> list[Role]:
        raise NotImplementedError

    def get_by_id(self, role_id: UUID) -> Role | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        permission_codes: tuple[str, ...],
    ) -> Role:
        raise NotImplementedError

    def set_permissions(self, role_id: UUID, permission_codes: tuple[str, ...]) -> Role:
        raise NotImplementedError


class RoleService:
    def __init__(self, roles: RoleStore) -> None:
        self._roles = roles

    def list_roles(self, organization_id: UUID) -> list[Role]:
        return self._roles.list(organization_id)

    def get_role(self, role_id: UUID) -> Role | None:
        return self._roles.get_by_id(role_id)

    def create_role(self, command: CreateRoleCommand) -> Role:
        return self._roles.create(
            organization_id=command.organization_id,
            name=command.name,
            description=command.description,
            permission_codes=command.permission_codes,
        )

    def set_role_permissions(self, role_id: UUID, permission_codes: tuple[str, ...]) -> Role:
        role = self._roles.get_by_id(role_id)
        if role is None:
            raise ValueError("role not found")
        if role.is_system:
            raise RoleNotEditableError("system roles cannot be modified")
        return self._roles.set_permissions(role_id, permission_codes)
