from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class ThreatCategory(StrEnum):
    HUMAN = "human"
    TECHNICAL = "technical"
    ENVIRONMENTAL = "environmental"
    ORGANIZATIONAL = "organizational"


class ThreatLikelihood(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class Threat:
    id: UUID
    organization_id: UUID
    name: str
    description: str
    category: ThreatCategory
    likelihood: ThreatLikelihood
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateThreatCommand:
    organization_id: UUID
    name: str
    category: ThreatCategory
    description: str = ""
    likelihood: ThreatLikelihood = ThreatLikelihood.MEDIUM
    created_by_id: UUID | None = None


class ThreatStore(Protocol):
    def list(self, organization_id: UUID) -> list[Threat]:
        raise NotImplementedError

    def get_by_id(self, threat_id: UUID) -> Threat | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        name: str,
        category: ThreatCategory,
        description: str,
        likelihood: ThreatLikelihood,
        created_by_id: UUID | None,
    ) -> Threat:
        raise NotImplementedError


class ThreatService:
    def __init__(self, threats: ThreatStore) -> None:
        self._threats = threats

    def list_threats(self, organization_id: UUID) -> list[Threat]:
        return self._threats.list(organization_id)

    def get_threat(self, threat_id: UUID) -> Threat | None:
        return self._threats.get_by_id(threat_id)

    def create_threat(self, command: CreateThreatCommand) -> Threat:
        return self._threats.create(
            organization_id=command.organization_id,
            name=command.name,
            category=command.category,
            description=command.description,
            likelihood=command.likelihood,
            created_by_id=command.created_by_id,
        )
