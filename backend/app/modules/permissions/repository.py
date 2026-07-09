from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.modules.permissions.models import PermissionModel
from backend.app.modules.permissions.service import Permission


def to_permission(model: PermissionModel) -> Permission:
    return Permission(
        id=model.id,
        code=model.code,
        description=model.description,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class PermissionRepository(ABC):
    @abstractmethod
    def list(self) -> list[Permission]:
        raise NotImplementedError


class SqlAlchemyPermissionRepository(PermissionRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self) -> list[Permission]:
        rows = self._session.scalars(select(PermissionModel).order_by(PermissionModel.code)).all()
        return [to_permission(row) for row in rows]
