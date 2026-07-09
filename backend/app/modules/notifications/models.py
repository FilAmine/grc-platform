from datetime import datetime
from uuid import UUID as PyUUID

from backend.app.common.models import TenantScopedMixin, TimestampMixin, UUIDPKMixin
from backend.app.database import Base
from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class NotificationModel(UUIDPKMixin, TenantScopedMixin, TimestampMixin, Base):
    __tablename__ = "notifications"

    recipient_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    subject: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    read_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
