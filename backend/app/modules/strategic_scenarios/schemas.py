from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.strategic_scenarios.service import StrategicScenarioLikelihood
from pydantic import Field


class StrategicScenarioCreate(ReadSchema):
    risk_origin_id: UUID
    feared_event_id: UUID
    name: str = Field(min_length=2, max_length=255)
    ecosystem_party_id: UUID | None = None
    description: str = Field(default="", max_length=4000)
    likelihood: StrategicScenarioLikelihood = StrategicScenarioLikelihood.MEDIUM


class StrategicScenarioRead(ReadSchema):
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
