from datetime import datetime
from uuid import UUID

from pydantic import Field

from backend.app.common.schemas import ReadSchema


class RoleCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=100)
    description: str = Field(default="", max_length=255)
    permission_codes: list[str] = Field(default_factory=list)


class RolePermissionsUpdate(ReadSchema):
    permission_codes: list[str]


class RoleRead(ReadSchema):
    id: UUID
    organization_id: UUID | None
    name: str
    description: str
    is_system: bool
    permission_codes: list[str]
    created_at: datetime
    updated_at: datetime
