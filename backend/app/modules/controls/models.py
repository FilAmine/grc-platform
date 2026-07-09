from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.controls.service import ControlStatus
from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class ControlModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "controls"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    framework: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[ControlStatus] = mapped_column(
        Enum(ControlStatus), default=ControlStatus.DRAFT, nullable=False
    )

    organization: Mapped["OrganizationModel"] = relationship(  # noqa: F821
        "OrganizationModel", back_populates="controls"
    )
