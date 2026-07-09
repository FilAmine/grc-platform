from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from pydantic import Field


class OrganizationCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    slug: str = Field(min_length=2, max_length=100, pattern=r"^[a-z0-9-]+$")


class OrganizationRead(ReadSchema):
    id: UUID
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
