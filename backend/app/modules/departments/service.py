from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class Department:
    id: UUID
    organization_id: UUID
    name: str
    description: str
    parent_department_id: UUID | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateDepartmentCommand:
    organization_id: UUID
    name: str
    description: str = ""
    parent_department_id: UUID | None = None
    created_by_id: UUID | None = None


class DepartmentStore(Protocol):
    def list(self, organization_id: UUID) -> list[Department]:
        raise NotImplementedError

    def get_by_id(self, department_id: UUID) -> Department | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        parent_department_id: UUID | None,
        created_by_id: UUID | None,
    ) -> Department:
        raise NotImplementedError


class DepartmentService:
    def __init__(self, departments: DepartmentStore) -> None:
        self._departments = departments

    def list_departments(self, organization_id: UUID) -> list[Department]:
        return self._departments.list(organization_id)

    def get_department(self, department_id: UUID) -> Department | None:
        return self._departments.get_by_id(department_id)

    def create_department(self, command: CreateDepartmentCommand) -> Department:
        # `parent_department_id` can only ever reference an already-persisted row
        # (ids are server-generated at INSERT, and there's no update/reparent
        # endpoint), so parent edges form a forest by construction -- no cycle
        # check needed. That invariant breaks the day a reparent endpoint is
        # added; revisit this then.
        return self._departments.create(
            organization_id=command.organization_id,
            name=command.name,
            description=command.description,
            parent_department_id=command.parent_department_id,
            created_by_id=command.created_by_id,
        )
