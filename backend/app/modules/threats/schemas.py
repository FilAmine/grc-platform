from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.threats.service import ThreatCategory, ThreatLikelihood
from pydantic import Field


class ThreatCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    category: ThreatCategory
    description: str = Field(default="", max_length=4000)
    likelihood: ThreatLikelihood = ThreatLikelihood.MEDIUM


class ThreatRead(ReadSchema):
    id: UUID
    organization_id: UUID
    name: str
    description: str
    category: ThreatCategory
    likelihood: ThreatLikelihood
    created_at: datetime
    updated_at: datetime
