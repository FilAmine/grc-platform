from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.strategic_scenarios.service import StrategicScenarioLikelihood
from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class StrategicScenarioModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "strategic_scenarios"

    # RESTRICT, not SET NULL: a strategic scenario *is* the elaboration of a
    # specific SR/OV pair targeting a specific feared event -- neither can
    # become null without the row losing its meaning, same reasoning as
    # risk_origins.risk_source_id.
    risk_origin_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("risk_origins.id", ondelete="RESTRICT"), index=True, nullable=False
    )
    feared_event_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("feared_events.id", ondelete="RESTRICT"), index=True, nullable=False
    )
    # Optional: not every attack path routes through a third party -- some
    # scenarios target the organization directly.
    ecosystem_party_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("ecosystem_parties.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    likelihood: Mapped[StrategicScenarioLikelihood] = mapped_column(
        Enum(StrategicScenarioLikelihood), default=StrategicScenarioLikelihood.MEDIUM, nullable=False
    )
