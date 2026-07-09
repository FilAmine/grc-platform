from uuid import UUID as PyUUID, uuid4

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.common.models import TimestampMixin
from backend.app.database import Base


class OrganizationModel(TimestampMixin, Base):
    __tablename__ = "organizations"

    id: Mapped[PyUUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    risks: Mapped[list["RiskModel"]] = relationship("RiskModel", back_populates="organization")
    controls: Mapped[list["ControlModel"]] = relationship("ControlModel", back_populates="organization")
