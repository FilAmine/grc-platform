from uuid import UUID as PyUUID

from backend.app.common.models import AuditColumnsMixin, TimestampMixin, UUIDPKMixin
from backend.app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, Table
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", PGUUID(as_uuid=True), ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "permission_id",
        PGUUID(as_uuid=True),
        ForeignKey("permissions.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class RoleModel(UUIDPKMixin, TimestampMixin, AuditColumnsMixin, Base):
    """A role is either a system role (``organization_id`` is ``NULL``, seeded once and
    shared by every tenant) or a custom role scoped to a single organization."""

    __tablename__ = "roles"

    organization_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    is_system: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    permissions: Mapped[list["PermissionModel"]] = relationship(  # noqa: F821
        "PermissionModel", secondary=role_permissions
    )
