from uuid import UUID as PyUUID, uuid4

from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.common.models import TimestampMixin
from backend.app.database import Base
from backend.app.modules.controls.service import ControlStatus


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

    organization: Mapped["OrganizationModel"] = relationship(
        "OrganizationModel", back_populates="controls"
    )
