from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.modules.organizations.models import OrganizationModel
from backend.app.modules.organizations.service import Organization


def to_organization(model: OrganizationModel) -> Organization:
    return Organization(
        id=model.id,
        name=model.name,
        slug=model.slug,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class OrganizationRepository(ABC):
    @abstractmethod
    def list(self) -> list[Organization]:
        raise NotImplementedError

    @abstractmethod
    def create(self, name: str, slug: str) -> Organization:
        raise NotImplementedError


class SqlAlchemyOrganizationRepository(OrganizationRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self) -> list[Organization]:
        rows = self._session.scalars(select(OrganizationModel).order_by(OrganizationModel.name)).all()
        return [to_organization(row) for row in rows]

    def create(self, name: str, slug: str) -> Organization:
        model = OrganizationModel(name=name, slug=slug)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_organization(model)
