from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.operational_scenarios.service import OperationalScenarioLikelihood
from pydantic import Field


class OperationalScenarioCreate(ReadSchema):
    strategic_scenario_id: UUID
    name: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)
    mitre_technique_ids: list[str] = Field(default_factory=list)
    technical_likelihood: OperationalScenarioLikelihood = OperationalScenarioLikelihood.MEDIUM


class OperationalScenarioRead(ReadSchema):
    id: UUID
    organization_id: UUID
    strategic_scenario_id: UUID
    name: str
    description: str
    mitre_technique_ids: list[str]
    technical_likelihood: OperationalScenarioLikelihood
    created_at: datetime
    updated_at: datetime
