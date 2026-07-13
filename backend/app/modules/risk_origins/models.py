from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.risk_origins.service import RiskOriginPertinence
from sqlalchemy import Boolean, Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class RiskOriginModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "risk_origins"

    # RESTRICT, not SET NULL: unlike Risk's 4 optional structural links, a
    # RiskOrigin *is* the SR/OV pairing -- a risk_source_id can't become NULL
    # without the row losing its entire meaning. Mirrors feared_events.asset_id's
    # RESTRICT reasoning (this app never hard-deletes risk_sources, only
    # soft-deletes via deleted_at, so this costs nothing in practice).
    risk_source_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("risk_sources.id", ondelete="RESTRICT"), index=True, nullable=False
    )
    target_objective: Mapped[str] = mapped_column(Text, nullable=False)
    # Optional: not every target objective maps to a pre-existing feared
    # event, unlike risk_source_id which is mandatory by definition.
    feared_event_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("feared_events.id", ondelete="SET NULL"), index=True, nullable=True
    )
    pertinence: Mapped[RiskOriginPertinence] = mapped_column(
        Enum(RiskOriginPertinence), default=RiskOriginPertinence.MEDIUM, nullable=False
    )
    retained: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
