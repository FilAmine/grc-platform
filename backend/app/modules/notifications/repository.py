from __future__ import annotations

from datetime import datetime
from uuid import UUID

from backend.app.modules.notifications.models import NotificationModel
from backend.app.modules.notifications.service import Notification
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_notification(model: NotificationModel) -> Notification:
    return Notification(
        id=model.id,
        organization_id=model.organization_id,
        recipient_id=model.recipient_id,
        subject=model.subject,
        body=model.body,
        read_at=model.read_at,
        created_at=model.created_at,
    )


class SqlAlchemyNotificationRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, organization_id: UUID, recipient_id: UUID, subject: str, body: str) -> Notification:
        model = NotificationModel(
            organization_id=organization_id, recipient_id=recipient_id, subject=subject, body=body
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_notification(model)

    def list_for_recipient(self, organization_id: UUID, recipient_id: UUID) -> list[Notification]:
        statement = (
            select(NotificationModel)
            .where(
                NotificationModel.organization_id == organization_id,
                NotificationModel.recipient_id == recipient_id,
            )
            .order_by(NotificationModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_notification(row) for row in rows]

    def mark_read(self, notification_id: UUID, now: datetime) -> Notification:
        model = self._session.get(NotificationModel, notification_id)
        if model is None:
            raise ValueError("notification not found")
        model.read_at = now
        self._session.commit()
        self._session.refresh(model)
        return to_notification(model)
