from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class Notification:
    recipient_id: UUID
    subject: str
    body: str
