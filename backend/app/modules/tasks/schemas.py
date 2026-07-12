from datetime import date, datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.tasks.service import TaskStatus
from pydantic import Field


class TaskCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    assignee: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)
    due_date: date | None = None


class TaskRead(ReadSchema):
    id: UUID
    organization_id: UUID
    title: str
    description: str
    status: TaskStatus
    due_date: date | None
    assignee: str
    created_at: datetime
    updated_at: datetime


class TaskStatusUpdate(ReadSchema):
    status: TaskStatus
