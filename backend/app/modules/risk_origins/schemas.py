from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.risk_origins.service import RiskOriginPertinence
from pydantic import Field


class RiskOriginCreate(ReadSchema):
    risk_source_id: UUID
    target_objective: str = Field(min_length=2, max_length=4000)
    feared_event_id: UUID | None = None
    pertinence: RiskOriginPertinence = RiskOriginPertinence.MEDIUM
    retained: bool = False


class RiskOriginRead(ReadSchema):
    id: UUID
    organization_id: UUID
    risk_source_id: UUID
    target_objective: str
    feared_event_id: UUID | None
    pertinence: RiskOriginPertinence
    retained: bool
    created_at: datetime
    updated_at: datetime
