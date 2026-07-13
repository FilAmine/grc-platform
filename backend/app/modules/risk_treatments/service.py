"""EBIOS RM Workshop 5: risk treatment -- the final workshop, synthesizing
a Workshop 3 strategic scenario (optionally detailed further by Workshop 4
operational scenarios) into a treatment decision.

`decision` is the standard 4-way ISO 27005 / EBIOS RM treatment choice
(avoid/reduce/transfer/accept). `residual_risk_level` is the risk level
*after* applying this treatment -- treatment doesn't eliminate risk, it
changes what's left over.

Deliberately list+create only, no update endpoint or status workflow --
matches every other EBIOS RM module built this session (RiskSource,
RiskOrigin, EcosystemParty, StrategicScenario, OperationalScenario). A
strategic scenario can have more than one RiskTreatment row over time
(no uniqueness constraint): re-deciding a treatment means creating a new
record, an append-only audit trail of the decision history, rather than
mutating one row in place.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class RiskTreatmentDecision(StrEnum):
    AVOID = "avoid"
    REDUCE = "reduce"
    TRANSFER = "transfer"
    ACCEPT = "accept"


class RiskTreatmentResidualRisk(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class RiskTreatment:
    id: UUID
    organization_id: UUID
    strategic_scenario_id: UUID
    decision: RiskTreatmentDecision
    justification: str
    residual_risk_level: RiskTreatmentResidualRisk
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateRiskTreatmentCommand:
    organization_id: UUID
    strategic_scenario_id: UUID
    decision: RiskTreatmentDecision
    justification: str = ""
    residual_risk_level: RiskTreatmentResidualRisk = RiskTreatmentResidualRisk.MEDIUM
    created_by_id: UUID | None = None


class RiskTreatmentStore(Protocol):
    def list(self, organization_id: UUID) -> list[RiskTreatment]:
        raise NotImplementedError

    def get_by_id(self, risk_treatment_id: UUID) -> RiskTreatment | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        strategic_scenario_id: UUID,
        decision: RiskTreatmentDecision,
        justification: str,
        residual_risk_level: RiskTreatmentResidualRisk,
        created_by_id: UUID | None,
    ) -> RiskTreatment:
        raise NotImplementedError


class RiskTreatmentService:
    def __init__(self, risk_treatments: RiskTreatmentStore) -> None:
        self._risk_treatments = risk_treatments

    def list_risk_treatments(self, organization_id: UUID) -> list[RiskTreatment]:
        return self._risk_treatments.list(organization_id)

    def get_risk_treatment(self, risk_treatment_id: UUID) -> RiskTreatment | None:
        return self._risk_treatments.get_by_id(risk_treatment_id)

    def create_risk_treatment(self, command: CreateRiskTreatmentCommand) -> RiskTreatment:
        return self._risk_treatments.create(
            organization_id=command.organization_id,
            strategic_scenario_id=command.strategic_scenario_id,
            decision=command.decision,
            justification=command.justification,
            residual_risk_level=command.residual_risk_level,
            created_by_id=command.created_by_id,
        )
