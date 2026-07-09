from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema


class NotificationRead(ReadSchema):
    id: UUID
    organization_id: UUID
    recipient_id: UUID
    subject: str
    body: str
    read_at: datetime | None
    created_at: datetime
