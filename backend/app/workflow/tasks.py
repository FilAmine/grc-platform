from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class WorkflowTask:
    id: UUID
    title: str
    assignee_id: UUID | None
    due_at: datetime | None
