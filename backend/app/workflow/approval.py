from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class ApprovalRequest:
    id: UUID
    subject: str
    requested_by: UUID
    requested_at: datetime
