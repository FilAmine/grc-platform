from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from backend.app.domain.entities import ControlStatus, RiskSeverity, RiskStatus


class OrganizationCreate(BaseModel):
    name: str = Field(min_length=2, max_length=255)
    slug: str = Field(min_length=2, max_length=100, pattern=r"^[a-z0-9-]+$")


class OrganizationRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime


class RiskCreate(BaseModel):
    organization_id: UUID
    title: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=1)
    severity: RiskSeverity
    owner: str = Field(min_length=2, max_length=255)


class RiskRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    organization_id: UUID
    title: str
    description: str
    severity: RiskSeverity
    status: RiskStatus
    owner: str
    created_at: datetime
    updated_at: datetime


class ControlCreate(BaseModel):
    organization_id: UUID
    name: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=1)
    framework: str = Field(min_length=2, max_length=100)


class ControlRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    organization_id: UUID
    name: str
    description: str
    framework: str
    status: ControlStatus
    created_at: datetime
    updated_at: datetime


class ComplianceSummary(BaseModel):
    organizations: int
    risks_open: int
    controls_active: int
    posture: str
