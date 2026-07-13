from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.risk_sources.service import (
    RiskSourceActivity,
    RiskSourceCategory,
    RiskSourceLevel,
)
from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class RiskSourceModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "risk_sources"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    category: Mapped[RiskSourceCategory] = mapped_column(Enum(RiskSourceCategory), nullable=False)
    motivation: Mapped[RiskSourceLevel] = mapped_column(
        Enum(RiskSourceLevel), default=RiskSourceLevel.MODERATE, nullable=False
    )
    resources: Mapped[RiskSourceLevel] = mapped_column(
        Enum(RiskSourceLevel), default=RiskSourceLevel.MODERATE, nullable=False
    )
    activity: Mapped[RiskSourceActivity] = mapped_column(
        Enum(RiskSourceActivity), default=RiskSourceActivity.MEDIUM, nullable=False
    )
