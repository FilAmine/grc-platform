"""EBIOS RM Workshop 2's "couple source de risque / objectif vise" (SR/OV
pair): pairs a RiskSource (risk_sources module -- who) with a target
objective (what they're after) and scores how pertinent/relevant that
pairing is to this organization. `retained` marks which pairs are
prioritized to carry forward into Workshop 3's strategic scenarios -- not
built here, see docs/roadmap.md.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class RiskOriginPertinence(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class RiskOrigin:
    id: UUID
    organization_id: UUID
    risk_source_id: UUID
    target_objective: str
    feared_event_id: UUID | None
    pertinence: RiskOriginPertinence
    retained: bool
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateRiskOriginCommand:
    organization_id: UUID
    risk_source_id: UUID
    target_objective: str
    feared_event_id: UUID | None = None
    pertinence: RiskOriginPertinence = RiskOriginPertinence.MEDIUM
    retained: bool = False
    created_by_id: UUID | None = None


class RiskOriginStore(Protocol):
    def list(self, organization_id: UUID) -> list[RiskOrigin]:
        raise NotImplementedError

    def get_by_id(self, risk_origin_id: UUID) -> RiskOrigin | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        risk_source_id: UUID,
        target_objective: str,
        feared_event_id: UUID | None,
        pertinence: RiskOriginPertinence,
        retained: bool,
        created_by_id: UUID | None,
    ) -> RiskOrigin:
        raise NotImplementedError


class RiskOriginService:
    def __init__(self, risk_origins: RiskOriginStore) -> None:
        self._risk_origins = risk_origins

    def list_risk_origins(self, organization_id: UUID) -> list[RiskOrigin]:
        return self._risk_origins.list(organization_id)

    def get_risk_origin(self, risk_origin_id: UUID) -> RiskOrigin | None:
        return self._risk_origins.get_by_id(risk_origin_id)

    def create_risk_origin(self, command: CreateRiskOriginCommand) -> RiskOrigin:
        return self._risk_origins.create(
            organization_id=command.organization_id,
            risk_source_id=command.risk_source_id,
            target_objective=command.target_objective,
            feared_event_id=command.feared_event_id,
            pertinence=command.pertinence,
            retained=command.retained,
            created_by_id=command.created_by_id,
        )
