from datetime import UTC, datetime
from uuid import UUID as PyUUID
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class UUIDPKMixin:
    id: Mapped[PyUUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid4)


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


class SoftDeleteMixin:
    """Rows are never hard-deleted; ``deleted_at`` marks them as retired.

    Repositories must filter ``deleted_at.is_(None)`` on every read.
    """

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None


class TenantScopedMixin:
    """Adds the tenant boundary column. The ``organizations`` table is the tenant root
    and does not carry this column itself."""

    @declared_attr
    def organization_id(cls) -> Mapped[PyUUID]:
        return mapped_column(
            PGUUID(as_uuid=True),
            ForeignKey("organizations.id", ondelete="CASCADE"),
            index=True,
            nullable=False,
        )


class AuditColumnsMixin:
    """Who created/last-modified a row. Nullable because the very first user of a
    tenant (created during self-service registration) has no prior actor to reference,
    and system/seed jobs may write rows with no acting user at all."""

    @declared_attr
    def created_by_id(cls) -> Mapped[PyUUID | None]:
        return mapped_column(
            PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
        )

    @declared_attr
    def updated_by_id(cls) -> Mapped[PyUUID | None]:
        return mapped_column(
            PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
        )
