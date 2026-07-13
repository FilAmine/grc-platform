from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class RiskSourceCategory(StrEnum):
    """ANSSI EBIOS RM Workshop 2's 7 standard risk-source categories."""

    STATE = "state"
    ORGANIZED_CRIME = "organized_crime"
    TERRORIST = "terrorist"
    ACTIVIST = "activist"
    VENGEFUL_INDIVIDUAL = "vengeful_individual"
    AMATEUR = "amateur"
    SPECIALIZED_FIRM = "specialized_firm"


class RiskSourceLevel(StrEnum):
    """Shared 4-level scale for motivation and resources -- ANSSI's Workshop 2
    evaluation grid scores both on the same scale."""

    LOW = "low"
    MODERATE = "moderate"
    SIGNIFICANT = "significant"
    VERY_HIGH = "very_high"


class RiskSourceActivity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class RiskSource:
    id: UUID
    organization_id: UUID
    name: str
    description: str
    category: RiskSourceCategory
    motivation: RiskSourceLevel
    resources: RiskSourceLevel
    activity: RiskSourceActivity
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateRiskSourceCommand:
    organization_id: UUID
    name: str
    category: RiskSourceCategory
    description: str = ""
    motivation: RiskSourceLevel = RiskSourceLevel.MODERATE
    resources: RiskSourceLevel = RiskSourceLevel.MODERATE
    activity: RiskSourceActivity = RiskSourceActivity.MEDIUM
    created_by_id: UUID | None = None


class RiskSourceStore(Protocol):
    def list(self, organization_id: UUID) -> list[RiskSource]:
        raise NotImplementedError

    def get_by_id(self, risk_source_id: UUID) -> RiskSource | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        name: str,
        category: RiskSourceCategory,
        description: str,
        motivation: RiskSourceLevel,
        resources: RiskSourceLevel,
        activity: RiskSourceActivity,
        created_by_id: UUID | None,
    ) -> RiskSource:
        raise NotImplementedError


class RiskSourceService:
    def __init__(self, risk_sources: RiskSourceStore) -> None:
        self._risk_sources = risk_sources

    def list_risk_sources(self, organization_id: UUID) -> list[RiskSource]:
        return self._risk_sources.list(organization_id)

    def get_risk_source(self, risk_source_id: UUID) -> RiskSource | None:
        return self._risk_sources.get_by_id(risk_source_id)

    def create_risk_source(self, command: CreateRiskSourceCommand) -> RiskSource:
        return self._risk_sources.create(
            organization_id=command.organization_id,
            name=command.name,
            category=command.category,
            description=command.description,
            motivation=command.motivation,
            resources=command.resources,
            activity=command.activity,
            created_by_id=command.created_by_id,
        )
