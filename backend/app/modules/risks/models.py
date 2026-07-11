from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.risks.service import RiskSeverity, RiskStatus
from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


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

    # EBIOS-RM-flavored structural links (all optional -- "risks" pre-existed
    # this feature, so nullable is required regardless of preference; see
    # docs/roadmap.md for exactly what this is and isn't modeling).
    asset_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("assets.id", ondelete="SET NULL"), index=True, nullable=True
    )
    threat_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("threats.id", ondelete="SET NULL"), index=True, nullable=True
    )
    vulnerability_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("vulnerabilities.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )
    feared_event_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("feared_events.id", ondelete="SET NULL"),
        index=True,
        nullable=True,
    )

    organization: Mapped["OrganizationModel"] = relationship(  # noqa: F821
        "OrganizationModel", back_populates="risks"
    )
