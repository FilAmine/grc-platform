from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class Permission:
    id: UUID
    code: str
    description: str
    created_at: datetime
    updated_at: datetime


class PermissionStore(Protocol):
    def list(self) -> list[Permission]:
        raise NotImplementedError


class PermissionService:
    def __init__(self, permissions: PermissionStore) -> None:
        self._permissions = permissions

    def list_permissions(self) -> list[Permission]:
        return self._permissions.list()
