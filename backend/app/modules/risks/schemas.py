from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.risks.service import RiskSeverity, RiskStatus
from pydantic import Field


class RiskCreate(ReadSchema):
    title: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=1)
    severity: RiskSeverity
    owner: str = Field(min_length=2, max_length=255)
    asset_id: UUID | None = None
    threat_id: UUID | None = None
    vulnerability_id: UUID | None = None
    feared_event_id: UUID | None = None


class RiskRead(ReadSchema):
    id: UUID
    organization_id: UUID
    title: str
    description: str
    severity: RiskSeverity
    status: RiskStatus
    owner: str
    created_at: datetime
    updated_at: datetime
    asset_id: UUID | None
    threat_id: UUID | None
    vulnerability_id: UUID | None
    feared_event_id: UUID | None
