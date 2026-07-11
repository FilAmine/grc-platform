from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.vulnerabilities.service import VulnerabilitySeverity, VulnerabilityStatus
from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class VulnerabilityModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "vulnerabilities"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    severity: Mapped[VulnerabilitySeverity] = mapped_column(Enum(VulnerabilitySeverity), nullable=False)
    status: Mapped[VulnerabilityStatus] = mapped_column(
        Enum(VulnerabilityStatus), default=VulnerabilityStatus.OPEN, nullable=False
    )
