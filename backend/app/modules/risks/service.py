from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class RiskStatus(StrEnum):
    OPEN = "open"
    MITIGATING = "mitigating"
    ACCEPTED = "accepted"
    CLOSED = "closed"


class RiskSeverity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class Risk:
    id: UUID
    organization_id: UUID
    title: str
    description: str
    severity: RiskSeverity
    status: RiskStatus
    owner: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateRiskCommand:
    organization_id: UUID
    title: str
    description: str
    severity: RiskSeverity
    owner: str


class RiskStore(Protocol):
    def list(self, organization_id: UUID | None = None) -> list[Risk]:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        title: str,
        description: str,
        severity: RiskSeverity,
        owner: str,
    ) -> Risk:
        raise NotImplementedError


class RiskService:
    def __init__(self, risks: RiskStore) -> None:
        self._risks = risks

    def list_risks(self, organization_id: UUID | None = None) -> list[Risk]:
        return self._risks.list(organization_id=organization_id)

    def create_risk(self, command: CreateRiskCommand) -> Risk:
        return self._risks.create(
            organization_id=command.organization_id,
            title=command.title,
            description=command.description,
            severity=command.severity,
            owner=command.owner,
        )
