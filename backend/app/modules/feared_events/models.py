from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.feared_events.service import FearedEventCriterion, FearedEventGravity
from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class FearedEventModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "feared_events"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    asset_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("assets.id", ondelete="RESTRICT"), index=True, nullable=False
    )
    criterion: Mapped[FearedEventCriterion] = mapped_column(Enum(FearedEventCriterion), nullable=False)
    gravity: Mapped[FearedEventGravity] = mapped_column(Enum(FearedEventGravity), nullable=False)
