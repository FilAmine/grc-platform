from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.common.models import TimestampMixin, UUIDPKMixin
from backend.app.database import Base


class PermissionModel(UUIDPKMixin, TimestampMixin, Base):
    """The RBAC permission catalog. Rows are seeded by migration from
    ``backend.app.security.permissions.ALL_PERMISSIONS`` and are not
    user-creatable via the API."""

    __tablename__ = "permissions"

    code: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
