"""EBIOS RM Workshop 4: operational scenarios. Elaborates a Workshop 3
strategic scenario (the "what and why") into a concrete technical attack
chain (the "how") -- ANSSI's methodology frames this as a cyber kill chain
of elementary technical actions, often mapped to MITRE ATT&CK techniques.

`mitre_technique_ids` is a plain list of free-text identifiers (e.g.
"T1566", "T1078"), not validated against a live MITRE ATT&CK catalog --
importing and maintaining that dataset (and keeping it in sync with
ATT&CK's own versioning) is a real, separate undertaking, out of scope
here. `technical_likelihood` is deliberately a separate field from the
linked strategic scenario's `likelihood`: that one captures whether an
attacker would pursue this path at all (motivation/targeting), this one
captures how technically feasible it is to actually pull off -- the two
can diverge (a highly motivated attacker facing a technically hard path,
or vice versa).
"""

# The Store Protocol below defines a method literally named `list`, which
# once bound shadows the builtin `list` for every later annotation in this
# same class body -- `create`'s `mitre_technique_ids: list[str]` parameter
# would otherwise resolve `list` to that method object, not the builtin
# generic. Deferring annotation evaluation sidesteps it; same fix already
# used by several other service.py/repository.py files in this codebase.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class OperationalScenarioLikelihood(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class OperationalScenario:
    id: UUID
    organization_id: UUID
    strategic_scenario_id: UUID
    name: str
    description: str
    mitre_technique_ids: list[str]
    technical_likelihood: OperationalScenarioLikelihood
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateOperationalScenarioCommand:
    organization_id: UUID
    strategic_scenario_id: UUID
    name: str
    description: str = ""
    mitre_technique_ids: list[str] | None = None
    technical_likelihood: OperationalScenarioLikelihood = OperationalScenarioLikelihood.MEDIUM
    created_by_id: UUID | None = None


class OperationalScenarioStore(Protocol):
    def list(self, organization_id: UUID) -> list[OperationalScenario]:
        raise NotImplementedError

    def get_by_id(self, operational_scenario_id: UUID) -> OperationalScenario | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        strategic_scenario_id: UUID,
        name: str,
        description: str,
        mitre_technique_ids: list[str],
        technical_likelihood: OperationalScenarioLikelihood,
        created_by_id: UUID | None,
    ) -> OperationalScenario:
        raise NotImplementedError


class OperationalScenarioService:
    def __init__(self, operational_scenarios: OperationalScenarioStore) -> None:
        self._operational_scenarios = operational_scenarios

    def list_operational_scenarios(self, organization_id: UUID) -> list[OperationalScenario]:
        return self._operational_scenarios.list(organization_id)

    def get_operational_scenario(self, operational_scenario_id: UUID) -> OperationalScenario | None:
        return self._operational_scenarios.get_by_id(operational_scenario_id)

    def create_operational_scenario(
        self, command: CreateOperationalScenarioCommand
    ) -> OperationalScenario:
        return self._operational_scenarios.create(
            organization_id=command.organization_id,
            strategic_scenario_id=command.strategic_scenario_id,
            name=command.name,
            description=command.description,
            mitre_technique_ids=command.mitre_technique_ids or [],
            technical_likelihood=command.technical_likelihood,
            created_by_id=command.created_by_id,
        )
