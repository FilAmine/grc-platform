from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.threats.service import ThreatCategory, ThreatLikelihood
from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class ThreatModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "threats"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    category: Mapped[ThreatCategory] = mapped_column(Enum(ThreatCategory), nullable=False)
    likelihood: Mapped[ThreatLikelihood] = mapped_column(
        Enum(ThreatLikelihood), default=ThreatLikelihood.MEDIUM, nullable=False
    )
