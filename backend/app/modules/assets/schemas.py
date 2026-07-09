from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.assets.service import AssetLifecycleStage, AssetType, ClassificationLevel
from pydantic import Field


class AssetCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    asset_type: AssetType
    owner: str = Field(min_length=2, max_length=255)
    description: str = Field(default="", max_length=4000)
    supplier: str = Field(default="", max_length=255)
    confidentiality: ClassificationLevel = ClassificationLevel.LOW
    integrity: ClassificationLevel = ClassificationLevel.LOW
    availability: ClassificationLevel = ClassificationLevel.LOW


class AssetLifecycleUpdate(ReadSchema):
    lifecycle_stage: AssetLifecycleStage


class AssetRead(ReadSchema):
    id: UUID
    organization_id: UUID
    name: str
    asset_type: AssetType
    description: str
    owner: str
    supplier: str
    lifecycle_stage: AssetLifecycleStage
    confidentiality: ClassificationLevel
    integrity: ClassificationLevel
    availability: ClassificationLevel
    created_at: datetime
    updated_at: datetime
