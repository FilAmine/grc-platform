from backend.app.interfaces.api.dependencies import (
    get_asset_service,
    get_current_user,
    get_feared_event_service,
    require_permission,
)
from backend.app.modules.assets.service import AssetService
from backend.app.modules.feared_events.schemas import FearedEventCreate, FearedEventRead
from backend.app.modules.feared_events.service import CreateFearedEventCommand, FearedEventService
from backend.app.modules.users.service import User
from backend.app.security.permissions import FEARED_EVENTS_MANAGE, FEARED_EVENTS_READ
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "",
    response_model=list[FearedEventRead],
    dependencies=[Depends(require_permission(FEARED_EVENTS_READ))],
)
def list_feared_events(
    current_user: User = Depends(get_current_user),
    service: FearedEventService = Depends(get_feared_event_service),
) -> list[FearedEventRead]:
    return [
        FearedEventRead.model_validate(item)
        for item in service.list_feared_events(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=FearedEventRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(FEARED_EVENTS_MANAGE))],
)
def create_feared_event(
    payload: FearedEventCreate,
    current_user: User = Depends(get_current_user),
    service: FearedEventService = Depends(get_feared_event_service),
    asset_service: AssetService = Depends(get_asset_service),
) -> FearedEventRead:
    asset = asset_service.get_asset(payload.asset_id)
    if asset is None or asset.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="asset not found")

    feared_event = service.create_feared_event(
        CreateFearedEventCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return FearedEventRead.model_validate(feared_event)
