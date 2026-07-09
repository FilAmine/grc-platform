from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.risks.service import RiskSeverity, RiskStatus


class RiskModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "risks"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    severity: Mapped[RiskSeverity] = mapped_column(Enum(RiskSeverity), nullable=False)
    status: Mapped[RiskStatus] = mapped_column(
        Enum(RiskStatus), default=RiskStatus.OPEN, nullable=False
    )
    owner: Mapped[str] = mapped_column(String(255), nullable=False)

    organization: Mapped["OrganizationModel"] = relationship(
        "OrganizationModel", back_populates="risks"
    )
