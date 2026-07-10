from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from pydantic import Field


class SsoConnectionUpdate(ReadSchema):
    issuer: str = Field(min_length=1, max_length=500)
    client_id: str = Field(min_length=1, max_length=255)
    client_secret: str = Field(min_length=1, max_length=500)
    default_role_id: UUID | None = None
    is_enabled: bool = True


class SsoConnectionRead(ReadSchema):
    id: UUID
    organization_id: UUID
    issuer: str
    client_id: str
    default_role_id: UUID | None
    is_enabled: bool
    created_at: datetime
    updated_at: datetime
