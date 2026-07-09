from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from backend.app.interfaces.api.dependencies import get_asset_service, get_current_user, require_permission
from backend.app.modules.assets.schemas import AssetCreate, AssetLifecycleUpdate, AssetRead
from backend.app.modules.assets.service import AssetService, CreateAssetCommand
from backend.app.modules.users.service import User
from backend.app.security.permissions import ASSETS_MANAGE, ASSETS_READ

router = APIRouter()


@router.get("", response_model=list[AssetRead], dependencies=[Depends(require_permission(ASSETS_READ))])
def list_assets(
    current_user: User = Depends(get_current_user),
    service: AssetService = Depends(get_asset_service),
) -> list[AssetRead]:
    return [AssetRead.model_validate(a) for a in service.list_assets(current_user.organization_id)]


@router.post(
    "", response_model=AssetRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(ASSETS_MANAGE))],
)
def create_asset(
    payload: AssetCreate,
    current_user: User = Depends(get_current_user),
    service: AssetService = Depends(get_asset_service),
) -> AssetRead:
    asset = service.create_asset(
        CreateAssetCommand(
            organization_id=current_user.organization_id, created_by_id=current_user.id, **payload.model_dump()
        )
    )
    return AssetRead.model_validate(asset)


@router.get("/{asset_id}", response_model=AssetRead, dependencies=[Depends(require_permission(ASSETS_READ))])
def get_asset(
    asset_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AssetService = Depends(get_asset_service),
) -> AssetRead:
    asset = service.get_asset(asset_id)
    if asset is None or asset.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="asset not found")
    return AssetRead.model_validate(asset)


@router.patch(
    "/{asset_id}/lifecycle", response_model=AssetRead,
    dependencies=[Depends(require_permission(ASSETS_MANAGE))],
)
def update_lifecycle_stage(
    asset_id: UUID,
    payload: AssetLifecycleUpdate,
    current_user: User = Depends(get_current_user),
    service: AssetService = Depends(get_asset_service),
) -> AssetRead:
    asset = service.get_asset(asset_id)
    if asset is None or asset.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="asset not found")
    return AssetRead.model_validate(service.set_lifecycle_stage(asset_id, payload.lifecycle_stage))
