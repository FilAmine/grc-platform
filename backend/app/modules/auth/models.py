from datetime import datetime
from uuid import UUID as PyUUID

from backend.app.common.models import TimestampMixin, UUIDPKMixin
from backend.app.database import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class RefreshTokenModel(UUIDPKMixin, TimestampMixin, Base):
    """Refresh tokens are stored hashed (sha256) so a leaked database dump does not
    hand out live sessions. Revocation happens by setting ``revoked_at``; refresh
    rotates the token (revokes the old row, inserts a new one)."""

    __tablename__ = "refresh_tokens"

    user_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    token_hash: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
