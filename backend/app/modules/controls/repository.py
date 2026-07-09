from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.modules.controls.models import ControlModel
from backend.app.modules.controls.service import Control
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_control(model: ControlModel) -> Control:
    return Control(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        framework=model.framework,
        status=model.status,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class ControlRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID | None = None) -> list[Control]:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        framework: str,
        created_by_id: UUID | None = None,
    ) -> Control:
        raise NotImplementedError


class SqlAlchemyControlRepository(ControlRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID | None = None) -> list[Control]:
        statement = (
            select(ControlModel)
            .where(ControlModel.deleted_at.is_(None))
            .order_by(ControlModel.name)
        )
        if organization_id:
            statement = statement.where(ControlModel.organization_id == organization_id)
        rows = self._session.scalars(statement).all()
        return [to_control(row) for row in rows]

    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        framework: str,
        created_by_id: UUID | None = None,
    ) -> Control:
        model = ControlModel(
            organization_id=organization_id,
            name=name,
            description=description,
            framework=framework,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_control(model)
