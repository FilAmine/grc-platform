from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TenantModel(UUIDPKMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base):
    """An optional grouping ABOVE organizations (e.g. a holding company with
    several subsidiary orgs) -- deliberately NOT `TenantScopedMixin` (that
    mixin's `organization_id` is the actual tenant-ISOLATION boundary every
    other module enforces; a `Tenant` here doesn't belong to an organization,
    organizations optionally belong to it, the reverse direction).

    Naming collision, stated plainly: after this, "tenant" means two things
    in this codebase -- (1) the existing, foundational meaning, the isolation
    boundary (`TenantScopedMixin`, "tenant isolation tests", every "tenant
    root" docstring -- unchanged, still `organization_id`), and (2) this
    entity, an optional grouping above organizations. See docs/database.md.
    """

    __tablename__ = "tenants"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    organizations: Mapped[list["OrganizationModel"]] = relationship(  # noqa: F821
        "OrganizationModel", back_populates="tenant"
    )
