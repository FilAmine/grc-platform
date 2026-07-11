from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from pydantic import Field


class DepartmentCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)
    parent_department_id: UUID | None = None


class DepartmentRead(ReadSchema):
    id: UUID
    organization_id: UUID
    name: str
    description: str
    parent_department_id: UUID | None
    created_at: datetime
    updated_at: datetime
