from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class OrganizationModel(UUIDPKMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base):
    """The tenant root. Every business object belongs to exactly one organization."""

    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    risks: Mapped[list["RiskModel"]] = relationship("RiskModel", back_populates="organization")  # noqa: F821
    controls: Mapped[list["ControlModel"]] = relationship(  # noqa: F821
        "ControlModel", back_populates="organization"
    )
