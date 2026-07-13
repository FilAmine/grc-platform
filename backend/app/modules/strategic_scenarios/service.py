"""EBIOS RM Workshop 3's strategic scenarios: elaborates a Workshop 2 SR/OV
pair (risk_origins) into a concrete, high-level attack path targeting a
specific feared event, optionally routed through an ecosystem party as a
stepping stone (ecosystem_parties) -- ANSSI's methodology treats attacking
via a third party as a first-class strategic-scenario shape, not a
footnote. Severity is deliberately NOT duplicated here: it's read off the
required `feared_event_id` link (that table's `gravity`) rather than copied
onto this row, avoiding a second source of truth that could drift.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class StrategicScenarioLikelihood(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class StrategicScenario:
    id: UUID
    organization_id: UUID
    risk_origin_id: UUID
    feared_event_id: UUID
    ecosystem_party_id: UUID | None
    name: str
    description: str
    likelihood: StrategicScenarioLikelihood
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateStrategicScenarioCommand:
    organization_id: UUID
    risk_origin_id: UUID
    feared_event_id: UUID
    name: str
    ecosystem_party_id: UUID | None = None
    description: str = ""
    likelihood: StrategicScenarioLikelihood = StrategicScenarioLikelihood.MEDIUM
    created_by_id: UUID | None = None


class StrategicScenarioStore(Protocol):
    def list(self, organization_id: UUID) -> list[StrategicScenario]:
        raise NotImplementedError

    def get_by_id(self, strategic_scenario_id: UUID) -> StrategicScenario | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        risk_origin_id: UUID,
        feared_event_id: UUID,
        name: str,
        ecosystem_party_id: UUID | None,
        description: str,
        likelihood: StrategicScenarioLikelihood,
        created_by_id: UUID | None,
    ) -> StrategicScenario:
        raise NotImplementedError


class StrategicScenarioService:
    def __init__(self, strategic_scenarios: StrategicScenarioStore) -> None:
        self._strategic_scenarios = strategic_scenarios

    def list_strategic_scenarios(self, organization_id: UUID) -> list[StrategicScenario]:
        return self._strategic_scenarios.list(organization_id)

    def get_strategic_scenario(self, strategic_scenario_id: UUID) -> StrategicScenario | None:
        return self._strategic_scenarios.get_by_id(strategic_scenario_id)

    def create_strategic_scenario(self, command: CreateStrategicScenarioCommand) -> StrategicScenario:
        return self._strategic_scenarios.create(
            organization_id=command.organization_id,
            risk_origin_id=command.risk_origin_id,
            feared_event_id=command.feared_event_id,
            name=command.name,
            ecosystem_party_id=command.ecosystem_party_id,
            description=command.description,
            likelihood=command.likelihood,
            created_by_id=command.created_by_id,
        )
