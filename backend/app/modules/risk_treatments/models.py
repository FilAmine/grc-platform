from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.risk_treatments.service import RiskTreatmentDecision, RiskTreatmentResidualRisk
from sqlalchemy import Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class RiskTreatmentModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "risk_treatments"

    # RESTRICT, not SET NULL: a risk treatment *is* a decision about a
    # specific strategic scenario -- same reasoning as every other EBIOS RM
    # FK chain this session (risk_origins.risk_source_id,
    # strategic_scenarios.risk_origin_id/feared_event_id,
    # operational_scenarios.strategic_scenario_id).
    strategic_scenario_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("strategic_scenarios.id", ondelete="RESTRICT"),
        index=True,
        nullable=False,
    )
    decision: Mapped[RiskTreatmentDecision] = mapped_column(Enum(RiskTreatmentDecision), nullable=False)
    justification: Mapped[str] = mapped_column(Text, nullable=False, default="")
    residual_risk_level: Mapped[RiskTreatmentResidualRisk] = mapped_column(
        Enum(RiskTreatmentResidualRisk), default=RiskTreatmentResidualRisk.MEDIUM, nullable=False
    )
