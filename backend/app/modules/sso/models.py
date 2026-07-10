from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class SsoConnectionModel(UUIDPKMixin, TenantScopedMixin, TimestampMixin, AuditColumnsMixin, Base):
    """One OIDC connection per organization. Config, not business data: hard
    delete via the API is fine (no SoftDeleteMixin)."""

    __tablename__ = "sso_connections"
    __table_args__ = (UniqueConstraint("organization_id", name="uq_sso_connections_organization_id"),)

    issuer: Mapped[str] = mapped_column(String(500), nullable=False)
    client_id: Mapped[str] = mapped_column(String(255), nullable=False)
    # Plaintext -- no KMS/envelope-encryption infra exists in this codebase.
    # See docs/security.md's SSO section for this known limitation.
    client_secret: Mapped[str] = mapped_column(String(500), nullable=False)
    default_role_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("roles.id", ondelete="SET NULL"), nullable=True
    )
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
