from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class VulnerabilitySeverity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class VulnerabilityStatus(StrEnum):
    OPEN = "open"
    MITIGATED = "mitigated"
    ACCEPTED = "accepted"
    CLOSED = "closed"


@dataclass(frozen=True)
class Vulnerability:
    id: UUID
    organization_id: UUID
    name: str
    description: str
    severity: VulnerabilitySeverity
    status: VulnerabilityStatus
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateVulnerabilityCommand:
    organization_id: UUID
    name: str
    severity: VulnerabilitySeverity
    description: str = ""
    created_by_id: UUID | None = None


class VulnerabilityStore(Protocol):
    def list(self, organization_id: UUID) -> list[Vulnerability]:
        raise NotImplementedError

    def get_by_id(self, vulnerability_id: UUID) -> Vulnerability | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        name: str,
        severity: VulnerabilitySeverity,
        description: str,
        created_by_id: UUID | None,
    ) -> Vulnerability:
        raise NotImplementedError


class VulnerabilityService:
    def __init__(self, vulnerabilities: VulnerabilityStore) -> None:
        self._vulnerabilities = vulnerabilities

    def list_vulnerabilities(self, organization_id: UUID) -> list[Vulnerability]:
        return self._vulnerabilities.list(organization_id)

    def get_vulnerability(self, vulnerability_id: UUID) -> Vulnerability | None:
        return self._vulnerabilities.get_by_id(vulnerability_id)

    def create_vulnerability(self, command: CreateVulnerabilityCommand) -> Vulnerability:
        return self._vulnerabilities.create(
            organization_id=command.organization_id,
            name=command.name,
            severity=command.severity,
            description=command.description,
            created_by_id=command.created_by_id,
        )
