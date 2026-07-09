from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class AssetType(StrEnum):
    HARDWARE = "hardware"
    SOFTWARE = "software"
    CLOUD_SERVICE = "cloud_service"
    APPLICATION = "application"
    BUSINESS_ASSET = "business_asset"
    SERVICE = "service"


class AssetLifecycleStage(StrEnum):
    PLANNED = "planned"
    IN_USE = "in_use"
    MAINTENANCE = "maintenance"
    RETIRED = "retired"
    DISPOSED = "disposed"


class ClassificationLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class Asset:
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


@dataclass(frozen=True)
class CreateAssetCommand:
    organization_id: UUID
    name: str
    asset_type: AssetType
    owner: str
    description: str = ""
    supplier: str = ""
    confidentiality: ClassificationLevel = ClassificationLevel.LOW
    integrity: ClassificationLevel = ClassificationLevel.LOW
    availability: ClassificationLevel = ClassificationLevel.LOW
    created_by_id: UUID | None = None


class AssetStore(Protocol):
    def list(self, organization_id: UUID) -> list[Asset]:
        raise NotImplementedError

    def get_by_id(self, asset_id: UUID) -> Asset | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        name: str,
        asset_type: AssetType,
        owner: str,
        description: str,
        supplier: str,
        confidentiality: ClassificationLevel,
        integrity: ClassificationLevel,
        availability: ClassificationLevel,
        created_by_id: UUID | None,
    ) -> Asset:
        raise NotImplementedError

    def set_lifecycle_stage(self, asset_id: UUID, stage: AssetLifecycleStage) -> Asset:
        raise NotImplementedError


class AssetService:
    def __init__(self, assets: AssetStore) -> None:
        self._assets = assets

    def list_assets(self, organization_id: UUID) -> list[Asset]:
        return self._assets.list(organization_id)

    def get_asset(self, asset_id: UUID) -> Asset | None:
        return self._assets.get_by_id(asset_id)

    def create_asset(self, command: CreateAssetCommand) -> Asset:
        return self._assets.create(
            organization_id=command.organization_id,
            name=command.name,
            asset_type=command.asset_type,
            owner=command.owner,
            description=command.description,
            supplier=command.supplier,
            confidentiality=command.confidentiality,
            integrity=command.integrity,
            availability=command.availability,
            created_by_id=command.created_by_id,
        )

    def set_lifecycle_stage(self, asset_id: UUID, stage: AssetLifecycleStage) -> Asset:
        return self._assets.set_lifecycle_stage(asset_id, stage)
