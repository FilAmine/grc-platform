from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class Notification:
    id: UUID
    organization_id: UUID
    recipient_id: UUID
    subject: str
    body: str
    read_at: datetime | None
    created_at: datetime


class NotificationStore(Protocol):
    def create(self, organization_id: UUID, recipient_id: UUID, subject: str, body: str) -> Notification:
        raise NotImplementedError

    def list_for_recipient(self, organization_id: UUID, recipient_id: UUID) -> list[Notification]:
        raise NotImplementedError

    def mark_read(self, notification_id: UUID, now: datetime) -> Notification:
        raise NotImplementedError


class NotificationSink(Protocol):
    """The narrow interface other modules depend on so they can trigger a
    notification without importing the whole notifications module."""

    def notify(self, organization_id: UUID, recipient_id: UUID, subject: str, body: str) -> None:
        raise NotImplementedError


class NotificationService:
    def __init__(self, notifications: NotificationStore) -> None:
        self._notifications = notifications

    def notify(self, organization_id: UUID, recipient_id: UUID, subject: str, body: str) -> None:
        self._notifications.create(organization_id, recipient_id, subject, body)

    def list_for_recipient(self, organization_id: UUID, recipient_id: UUID) -> list[Notification]:
        return self._notifications.list_for_recipient(organization_id, recipient_id)

    def mark_read(self, notification_id: UUID, now: datetime) -> Notification:
        return self._notifications.mark_read(notification_id, now)
