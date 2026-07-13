from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.risk_sources.service import (
    RiskSourceActivity,
    RiskSourceCategory,
    RiskSourceLevel,
)
from pydantic import Field


class RiskSourceCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    category: RiskSourceCategory
    description: str = Field(default="", max_length=4000)
    motivation: RiskSourceLevel = RiskSourceLevel.MODERATE
    resources: RiskSourceLevel = RiskSourceLevel.MODERATE
    activity: RiskSourceActivity = RiskSourceActivity.MEDIUM


class RiskSourceRead(ReadSchema):
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
