from sqlalchemy import Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.assets.service import AssetLifecycleStage, AssetType, ClassificationLevel


class AssetModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "assets"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    asset_type: Mapped[AssetType] = mapped_column(Enum(AssetType), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    owner: Mapped[str] = mapped_column(String(255), nullable=False)
    supplier: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    lifecycle_stage: Mapped[AssetLifecycleStage] = mapped_column(
        Enum(AssetLifecycleStage), default=AssetLifecycleStage.PLANNED, nullable=False
    )
    confidentiality: Mapped[ClassificationLevel] = mapped_column(
        Enum(ClassificationLevel, name="classificationlevel"), default=ClassificationLevel.LOW, nullable=False
    )
    integrity: Mapped[ClassificationLevel] = mapped_column(
        Enum(ClassificationLevel, name="classificationlevel"), default=ClassificationLevel.LOW, nullable=False
    )
    availability: Mapped[ClassificationLevel] = mapped_column(
        Enum(ClassificationLevel, name="classificationlevel"), default=ClassificationLevel.LOW, nullable=False
    )
