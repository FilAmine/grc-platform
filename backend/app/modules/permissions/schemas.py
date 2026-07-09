from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema


class PermissionRead(ReadSchema):
    id: UUID
    code: str
    description: str
    created_at: datetime
    updated_at: datetime
