from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.modules.departments.models import DepartmentModel
from backend.app.modules.departments.service import Department
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_department(model: DepartmentModel) -> Department:
    return Department(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        parent_department_id=model.parent_department_id,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class DepartmentRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID) -> list[Department]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, department_id: UUID) -> Department | None:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        parent_department_id: UUID | None,
        created_by_id: UUID | None,
    ) -> Department:
        raise NotImplementedError


class SqlAlchemyDepartmentRepository(DepartmentRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Department]:
        statement = (
            select(DepartmentModel)
            .where(DepartmentModel.deleted_at.is_(None))
            .where(DepartmentModel.organization_id == organization_id)
            .order_by(DepartmentModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_department(row) for row in rows]

    def get_by_id(self, department_id: UUID) -> Department | None:
        model = self._session.get(DepartmentModel, department_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_department(model)

    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        parent_department_id: UUID | None,
        created_by_id: UUID | None,
    ) -> Department:
        model = DepartmentModel(
            organization_id=organization_id,
            name=name,
            description=description,
            parent_department_id=parent_department_id,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_department(model)
