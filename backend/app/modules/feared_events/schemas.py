from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.feared_events.service import FearedEventCriterion, FearedEventGravity
from pydantic import Field


class FearedEventCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    asset_id: UUID
    criterion: FearedEventCriterion
    gravity: FearedEventGravity
    description: str = Field(default="", max_length=4000)


class FearedEventRead(ReadSchema):
    id: UUID
    organization_id: UUID
    title: str
    description: str
    asset_id: UUID
    criterion: FearedEventCriterion
    gravity: FearedEventGravity
    created_at: datetime
    updated_at: datetime
