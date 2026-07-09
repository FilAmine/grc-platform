from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, Field

from backend.app.common.schemas import ReadSchema
from backend.app.modules.compliance.service import AssessmentStatus, RequirementResultStatus


class ComplianceSummary(BaseModel):
    organizations: int
    risks_open: int
    controls_active: int
    posture: str


class FrameworkCreate(ReadSchema):
    code: str = Field(min_length=2, max_length=100)
    name: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)


class FrameworkRead(ReadSchema):
    id: UUID
    organization_id: UUID | None
    code: str
    name: str
    description: str
    is_system: bool
    created_at: datetime
    updated_at: datetime


class FrameworkVersionCreate(ReadSchema):
    version: str = Field(min_length=1, max_length=50)
    published_at: date | None = None


class FrameworkVersionRead(ReadSchema):
    id: UUID
    framework_id: UUID
    version: str
    published_at: date | None
    created_at: datetime
    updated_at: datetime


class RequirementCreate(ReadSchema):
    code: str = Field(min_length=1, max_length=50)
    title: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)
    category_id: UUID | None = None


class RequirementRead(ReadSchema):
    id: UUID
    framework_version_id: UUID
    category_id: UUID | None
    code: str
    title: str
    description: str
    created_at: datetime
    updated_at: datetime


class ControlMappingRead(ReadSchema):
    id: UUID
    control_id: UUID
    requirement_id: UUID
    created_at: datetime


class AssessmentCreate(ReadSchema):
    framework_version_id: UUID
    name: str = Field(min_length=2, max_length=255)
    period_start: date | None = None
    period_end: date | None = None


class AssessmentRead(ReadSchema):
    id: UUID
    organization_id: UUID
    framework_version_id: UUID
    name: str
    status: AssessmentStatus
    period_start: date | None
    period_end: date | None
    created_at: datetime
    updated_at: datetime


class AssessmentStatusUpdate(ReadSchema):
    status: AssessmentStatus


class AssessmentResultUpdate(ReadSchema):
    status: RequirementResultStatus
    notes: str = Field(default="", max_length=4000)


class AssessmentResultRead(ReadSchema):
    id: UUID
    assessment_id: UUID
    requirement_id: UUID
    status: RequirementResultStatus
    notes: str
    created_at: datetime
    updated_at: datetime


class EvidenceCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)
    file_reference: str = Field(min_length=1, max_length=1024)
    assessment_result_id: UUID | None = None
    control_id: UUID | None = None


class EvidenceRead(ReadSchema):
    id: UUID
    organization_id: UUID
    assessment_result_id: UUID | None
    control_id: UUID | None
    title: str
    description: str
    file_reference: str
    uploaded_by_id: UUID | None
    created_at: datetime
    updated_at: datetime


class ComplianceScoreRead(ReadSchema):
    id: UUID
    organization_id: UUID
    assessment_id: UUID
    framework_version_id: UUID
    score: float
    computed_at: datetime
