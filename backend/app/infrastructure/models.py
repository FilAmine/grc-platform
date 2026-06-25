from datetime import UTC, datetime
from uuid import UUID as PyUUID, uuid4

from sqlalchemy import DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.domain.entities import ControlStatus, RiskSeverity, RiskStatus
from backend.app.infrastructure.database import Base


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False,
    )


class OrganizationModel(TimestampMixin, Base):
    __tablename__ = "organizations"

    id: Mapped[PyUUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    risks: Mapped[list["RiskModel"]] = relationship(back_populates="organization")
    controls: Mapped[list["ControlModel"]] = relationship(back_populates="organization")


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

    organization: Mapped[OrganizationModel] = relationship(back_populates="risks")


class ControlModel(TimestampMixin, Base):
    __tablename__ = "controls"

    id: Mapped[PyUUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    organization_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("organizations.id"), index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    framework: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[ControlStatus] = mapped_column(
        Enum(ControlStatus), default=ControlStatus.DRAFT, nullable=False
    )

    organization: Mapped[OrganizationModel] = relationship(back_populates="controls")
