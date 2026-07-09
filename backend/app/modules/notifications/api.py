from datetime import UTC, datetime
from uuid import UUID

from backend.app.interfaces.api.dependencies import get_current_user, get_notification_service
from backend.app.modules.notifications.schemas import NotificationRead
from backend.app.modules.notifications.service import NotificationService
from backend.app.modules.users.service import User
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[NotificationRead])
def list_my_notifications(
    current_user: User = Depends(get_current_user),
    service: NotificationService = Depends(get_notification_service),
) -> list[NotificationRead]:
    return [
        NotificationRead.model_validate(n)
        for n in service.list_for_recipient(current_user.organization_id, current_user.id)
    ]


@router.post("/{notification_id}/read", response_model=NotificationRead)
def mark_notification_read(
    notification_id: UUID,
    service: NotificationService = Depends(get_notification_service),
) -> NotificationRead:
    return NotificationRead.model_validate(service.mark_read(notification_id, datetime.now(UTC)))
