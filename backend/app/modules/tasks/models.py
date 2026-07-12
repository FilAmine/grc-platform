from datetime import date

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.tasks.service import TaskStatus
from sqlalchemy import Date, Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class TaskModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.OPEN, nullable=False)
    due_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    assignee: Mapped[str] = mapped_column(String(255), nullable=False)
