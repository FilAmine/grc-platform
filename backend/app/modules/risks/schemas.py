from datetime import datetime
from uuid import UUID

from pydantic import Field

from backend.app.common.schemas import ReadSchema
from backend.app.modules.risks.service import RiskSeverity, RiskStatus


class RiskCreate(ReadSchema):
    title: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=1)
    severity: RiskSeverity
    owner: str = Field(min_length=2, max_length=255)


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
