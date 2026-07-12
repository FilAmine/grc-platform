from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.modules.tenants.models import TenantModel
from backend.app.modules.tenants.service import Tenant
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_tenant(model: TenantModel) -> Tenant:
    return Tenant(
        id=model.id,
        name=model.name,
        slug=model.slug,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class TenantRepository(ABC):
    @abstractmethod
    def list(self) -> list[Tenant]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, tenant_id: UUID) -> Tenant | None:
        raise NotImplementedError

    @abstractmethod
    def create(self, name: str, slug: str) -> Tenant:
        raise NotImplementedError


class SqlAlchemyTenantRepository(TenantRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self) -> list[Tenant]:
        statement = (
            select(TenantModel).where(TenantModel.deleted_at.is_(None)).order_by(TenantModel.name)
        )
        rows = self._session.scalars(statement).all()
        return [to_tenant(row) for row in rows]

    def get_by_id(self, tenant_id: UUID) -> Tenant | None:
        model = self._session.get(TenantModel, tenant_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_tenant(model)

    def create(self, name: str, slug: str) -> Tenant:
        model = TenantModel(name=name, slug=slug)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_tenant(model)
