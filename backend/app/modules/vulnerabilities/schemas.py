from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.vulnerabilities.service import VulnerabilitySeverity, VulnerabilityStatus
from pydantic import Field


class VulnerabilityCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    severity: VulnerabilitySeverity
    description: str = Field(default="", max_length=4000)


class VulnerabilityRead(ReadSchema):
    id: UUID
    organization_id: UUID
    name: str
    description: str
    severity: VulnerabilitySeverity
    status: VulnerabilityStatus
    created_at: datetime
    updated_at: datetime
