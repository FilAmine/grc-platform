from datetime import date, datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.audits.service import (
    AuditStatus,
    ChecklistItemStatus,
    CorrectiveActionStatus,
    FindingSeverity,
    FindingStatus,
)
from pydantic import BaseModel, Field


class AuditCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    scope: str = Field(default="", max_length=4000)
    lead_auditor: str = Field(min_length=2, max_length=255)
    period_start: date | None = None
    period_end: date | None = None


class AuditRead(ReadSchema):
    id: UUID
    organization_id: UUID
    title: str
    scope: str
    lead_auditor: str
    status: AuditStatus
    period_start: date | None
    period_end: date | None
    created_at: datetime
    updated_at: datetime


class AuditStatusUpdate(ReadSchema):
    status: AuditStatus


class ChecklistItemCreate(ReadSchema):
    description: str = Field(min_length=2, max_length=4000)


class ChecklistItemStatusUpdate(ReadSchema):
    status: ChecklistItemStatus
    notes: str = Field(default="", max_length=4000)


class ChecklistItemRead(ReadSchema):
    id: UUID
    audit_id: UUID
    description: str
    status: ChecklistItemStatus
    notes: str
    created_at: datetime
    updated_at: datetime


class FindingCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    description: str = Field(min_length=1, max_length=4000)
    severity: FindingSeverity
    checklist_item_id: UUID | None = None


class FindingStatusUpdate(ReadSchema):
    status: FindingStatus


class FindingRead(ReadSchema):
    id: UUID
    audit_id: UUID
    checklist_item_id: UUID | None
    title: str
    description: str
    severity: FindingSeverity
    status: FindingStatus
    created_at: datetime
    updated_at: datetime


class CorrectiveActionCreate(ReadSchema):
    description: str = Field(min_length=2, max_length=4000)
    owner: str = Field(min_length=2, max_length=255)
    due_date: date | None = None


class CorrectiveActionStatusUpdate(ReadSchema):
    status: CorrectiveActionStatus


class CorrectiveActionRead(ReadSchema):
    id: UUID
    finding_id: UUID
    description: str
    owner: str
    due_date: date | None
    status: CorrectiveActionStatus
    completed_at: datetime | None
    created_at: datetime
    updated_at: datetime


class AuditReportRead(BaseModel):
    audit: AuditRead
    checklist_total: int
    checklist_done: int
    findings_by_severity: dict[str, int]
    open_findings: int
    corrective_actions_total: int
    corrective_actions_done: int
