from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.ecosystem_parties.service import EcosystemPartyCategory, EcosystemPartyLevel
from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column


class EcosystemPartyModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "ecosystem_parties"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    category: Mapped[EcosystemPartyCategory] = mapped_column(Enum(EcosystemPartyCategory), nullable=False)
    dependency_level: Mapped[EcosystemPartyLevel] = mapped_column(
        Enum(EcosystemPartyLevel), default=EcosystemPartyLevel.MEDIUM, nullable=False
    )
    cyber_maturity: Mapped[EcosystemPartyLevel] = mapped_column(
        Enum(EcosystemPartyLevel), default=EcosystemPartyLevel.MEDIUM, nullable=False
    )
