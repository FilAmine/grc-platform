from datetime import datetime
from uuid import UUID

from pydantic import Field

from backend.app.common.schemas import ReadSchema
from backend.app.modules.controls.service import ControlStatus


class ControlCreate(ReadSchema):
    organization_id: UUID
    name: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=1)
    framework: str = Field(min_length=2, max_length=100)


class ControlRead(ReadSchema):
    id: UUID
    organization_id: UUID
    name: str
    description: str
    framework: str
    status: ControlStatus
    created_at: datetime
    updated_at: datetime
