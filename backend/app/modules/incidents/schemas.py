from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.incidents.service import IncidentSeverity, IncidentStatus
from pydantic import Field


class IncidentCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    severity: IncidentSeverity
    reported_by: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)


class IncidentRead(ReadSchema):
    id: UUID
    organization_id: UUID
    title: str
    description: str
    severity: IncidentSeverity
    status: IncidentStatus
    reported_by: str
    resolved_at: datetime | None
    created_at: datetime
    updated_at: datetime


class IncidentStatusUpdate(ReadSchema):
    status: IncidentStatus
