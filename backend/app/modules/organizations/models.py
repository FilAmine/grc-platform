from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class OrganizationModel(UUIDPKMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base):
    """The tenant ISOLATION root -- every `TenantScopedMixin` business object
    belongs to exactly one organization, and that boundary is unaffected by
    `tenant_id` below. `tenant_id` is a *different* concept: an optional
    grouping of several organizations under one `Tenant` record (see
    `modules/tenants/models.py`'s docstring for the full disambiguation)."""

    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    tenant_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("tenants.id", ondelete="SET NULL"), index=True, nullable=True
    )

    tenant: Mapped["TenantModel | None"] = relationship(  # noqa: F821
        "TenantModel", back_populates="organizations"
    )
    risks: Mapped[list["RiskModel"]] = relationship("RiskModel", back_populates="organization")  # noqa: F821
    controls: Mapped[list["ControlModel"]] = relationship(  # noqa: F821
        "ControlModel", back_populates="organization"
    )
