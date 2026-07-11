from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.modules.threats.models import ThreatModel
from backend.app.modules.threats.service import Threat, ThreatCategory, ThreatLikelihood
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_threat(model: ThreatModel) -> Threat:
    return Threat(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        category=model.category,
        likelihood=model.likelihood,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class ThreatRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID) -> list[Threat]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, threat_id: UUID) -> Threat | None:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        name: str,
        category: ThreatCategory,
        description: str,
        likelihood: ThreatLikelihood,
        created_by_id: UUID | None,
    ) -> Threat:
        raise NotImplementedError


class SqlAlchemyThreatRepository(ThreatRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Threat]:
        statement = (
            select(ThreatModel)
            .where(ThreatModel.deleted_at.is_(None))
            .where(ThreatModel.organization_id == organization_id)
            .order_by(ThreatModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_threat(row) for row in rows]

    def get_by_id(self, threat_id: UUID) -> Threat | None:
        model = self._session.get(ThreatModel, threat_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_threat(model)

    def create(
        self,
        organization_id: UUID,
        name: str,
        category: ThreatCategory,
        description: str,
        likelihood: ThreatLikelihood,
        created_by_id: UUID | None,
    ) -> Threat:
        model = ThreatModel(
            organization_id=organization_id,
            name=name,
            category=category,
            description=description,
            likelihood=likelihood,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_threat(model)
