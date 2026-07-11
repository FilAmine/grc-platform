from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID

from backend.app.workflow.state_machine import StateMachine, Transition


class IncidentSeverity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class IncidentStatus(StrEnum):
    OPEN = "open"
    INVESTIGATING = "investigating"
    RESOLVED = "resolved"
    CLOSED = "closed"


INCIDENT_STATUS_MACHINE: StateMachine[IncidentStatus] = StateMachine(
    [
        Transition("investigate", IncidentStatus.OPEN, IncidentStatus.INVESTIGATING),
        Transition("resolve", IncidentStatus.INVESTIGATING, IncidentStatus.RESOLVED),
        Transition("close", IncidentStatus.RESOLVED, IncidentStatus.CLOSED),
        Transition("reopen", IncidentStatus.RESOLVED, IncidentStatus.INVESTIGATING),
    ]
)


@dataclass(frozen=True)
class Incident:
    id: UUID
    organization_id: UUID
    title: str
    description: str
    severity: IncidentSeverity
    status: IncidentStatus
    reported_by: str
    resolved_at: datetime | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateIncidentCommand:
    organization_id: UUID
    title: str
    severity: IncidentSeverity
    reported_by: str
    description: str = ""
    created_by_id: UUID | None = None


class IncidentNotFoundError(Exception):
    pass


class IncidentStore(Protocol):
    def list(self, organization_id: UUID) -> list[Incident]:
        raise NotImplementedError

    def get_by_id(self, incident_id: UUID) -> Incident | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        title: str,
        severity: IncidentSeverity,
        reported_by: str,
        description: str,
        created_by_id: UUID | None,
    ) -> Incident:
        raise NotImplementedError

    def set_status(
        self, incident_id: UUID, status: IncidentStatus, resolved_at: datetime | None
    ) -> Incident:
        raise NotImplementedError


class IncidentService:
    def __init__(self, incidents: IncidentStore) -> None:
        self._incidents = incidents

    def list_incidents(self, organization_id: UUID) -> list[Incident]:
        return self._incidents.list(organization_id)

    def get_incident(self, incident_id: UUID) -> Incident | None:
        return self._incidents.get_by_id(incident_id)

    def create_incident(self, command: CreateIncidentCommand) -> Incident:
        return self._incidents.create(
            organization_id=command.organization_id,
            title=command.title,
            severity=command.severity,
            reported_by=command.reported_by,
            description=command.description,
            created_by_id=command.created_by_id,
        )

    def set_status(self, incident_id: UUID, status: IncidentStatus, now: datetime) -> Incident:
        current = self._incidents.get_by_id(incident_id)
        if current is None:
            raise IncidentNotFoundError("incident not found")
        INCIDENT_STATUS_MACHINE.transition_to(current.status, status)
        resolved_at = now if status == IncidentStatus.RESOLVED else None
        return self._incidents.set_status(incident_id, status, resolved_at)
