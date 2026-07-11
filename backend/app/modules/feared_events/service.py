from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class FearedEventCriterion(StrEnum):
    CONFIDENTIALITY = "confidentiality"
    INTEGRITY = "integrity"
    AVAILABILITY = "availability"


class FearedEventGravity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class FearedEvent:
    id: UUID
    organization_id: UUID
    title: str
    description: str
    asset_id: UUID
    criterion: FearedEventCriterion
    gravity: FearedEventGravity
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateFearedEventCommand:
    organization_id: UUID
    title: str
    asset_id: UUID
    criterion: FearedEventCriterion
    gravity: FearedEventGravity
    description: str = ""
    created_by_id: UUID | None = None


class FearedEventStore(Protocol):
    def list(self, organization_id: UUID) -> list[FearedEvent]:
        raise NotImplementedError

    def get_by_id(self, feared_event_id: UUID) -> FearedEvent | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        title: str,
        asset_id: UUID,
        criterion: FearedEventCriterion,
        gravity: FearedEventGravity,
        description: str,
        created_by_id: UUID | None,
    ) -> FearedEvent:
        raise NotImplementedError


class FearedEventService:
    def __init__(self, feared_events: FearedEventStore) -> None:
        self._feared_events = feared_events

    def list_feared_events(self, organization_id: UUID) -> list[FearedEvent]:
        return self._feared_events.list(organization_id)

    def get_feared_event(self, feared_event_id: UUID) -> FearedEvent | None:
        return self._feared_events.get_by_id(feared_event_id)

    def create_feared_event(self, command: CreateFearedEventCommand) -> FearedEvent:
        return self._feared_events.create(
            organization_id=command.organization_id,
            title=command.title,
            asset_id=command.asset_id,
            criterion=command.criterion,
            gravity=command.gravity,
            description=command.description,
            created_by_id=command.created_by_id,
        )
