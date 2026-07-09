from __future__ import annotations

from uuid import UUID

from backend.app.modules.assets.models import AssetModel
from backend.app.modules.assets.service import (
    Asset,
    AssetLifecycleStage,
    AssetType,
    ClassificationLevel,
)
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_asset(model: AssetModel) -> Asset:
    return Asset(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        asset_type=model.asset_type,
        description=model.description,
        owner=model.owner,
        supplier=model.supplier,
        lifecycle_stage=model.lifecycle_stage,
        confidentiality=model.confidentiality,
        integrity=model.integrity,
        availability=model.availability,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyAssetRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Asset]:
        statement = (
            select(AssetModel)
            .where(AssetModel.organization_id == organization_id, AssetModel.deleted_at.is_(None))
            .order_by(AssetModel.name)
        )
        rows = self._session.scalars(statement).all()
        return [to_asset(row) for row in rows]

    def get_by_id(self, asset_id: UUID) -> Asset | None:
        model = self._session.get(AssetModel, asset_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_asset(model)

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
        model = AssetModel(
            organization_id=organization_id,
            name=name,
            asset_type=asset_type,
            owner=owner,
            description=description,
            supplier=supplier,
            confidentiality=confidentiality,
            integrity=integrity,
            availability=availability,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_asset(model)

    def set_lifecycle_stage(self, asset_id: UUID, stage: AssetLifecycleStage) -> Asset:
        model = self._session.get(AssetModel, asset_id)
        if model is None:
            raise ValueError("asset not found")
        model.lifecycle_stage = stage
        self._session.commit()
        self._session.refresh(model)
        return to_asset(model)
