from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class ControlStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    RETIRED = "retired"


@dataclass(frozen=True)
class Control:
    id: UUID
    organization_id: UUID
    name: str
    description: str
    framework: str
    status: ControlStatus
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateControlCommand:
    organization_id: UUID
    name: str
    description: str
    framework: str
    created_by_id: UUID | None = None


class ControlStore(Protocol):
    def list(self, organization_id: UUID | None = None) -> list[Control]:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        framework: str,
        created_by_id: UUID | None = None,
    ) -> Control:
        raise NotImplementedError


class ControlService:
    def __init__(self, controls: ControlStore) -> None:
        self._controls = controls

    def list_controls(self, organization_id: UUID | None = None) -> list[Control]:
        return self._controls.list(organization_id=organization_id)

    def create_control(self, command: CreateControlCommand) -> Control:
        return self._controls.create(
            organization_id=command.organization_id,
            name=command.name,
            description=command.description,
            framework=command.framework,
            created_by_id=command.created_by_id,
        )
