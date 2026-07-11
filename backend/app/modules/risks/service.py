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
    asset_id: UUID | None = None
    threat_id: UUID | None = None
    vulnerability_id: UUID | None = None
    feared_event_id: UUID | None = None


@dataclass(frozen=True)
class CreateRiskCommand:
    organization_id: UUID
    title: str
    description: str
    severity: RiskSeverity
    owner: str
    created_by_id: UUID | None = None
    asset_id: UUID | None = None
    threat_id: UUID | None = None
    vulnerability_id: UUID | None = None
    feared_event_id: UUID | None = None


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
        created_by_id: UUID | None = None,
        asset_id: UUID | None = None,
        threat_id: UUID | None = None,
        vulnerability_id: UUID | None = None,
        feared_event_id: UUID | None = None,
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
            created_by_id=command.created_by_id,
            asset_id=command.asset_id,
            threat_id=command.threat_id,
            vulnerability_id=command.vulnerability_id,
            feared_event_id=command.feared_event_id,
        )
