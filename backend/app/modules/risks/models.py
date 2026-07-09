from uuid import UUID as PyUUID, uuid4

from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.common.models import TimestampMixin
from backend.app.database import Base
from backend.app.modules.risks.service import RiskSeverity, RiskStatus


class RiskModel(TimestampMixin, Base):
    __tablename__ = "risks"

    id: Mapped[PyUUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    organization_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("organizations.id"), index=True, nullable=False
    )
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
