from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.modules.risks.models import RiskModel
from backend.app.modules.risks.service import Risk, RiskSeverity, RiskStatus
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_risk(model: RiskModel) -> Risk:
    return Risk(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        description=model.description,
        severity=model.severity,
        status=model.status,
        owner=model.owner,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class RiskRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID | None = None) -> list[Risk]:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        title: str,
        description: str,
        severity: RiskSeverity,
        owner: str,
        created_by_id: UUID | None = None,
    ) -> Risk:
        raise NotImplementedError


class SqlAlchemyRiskRepository(RiskRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID | None = None) -> list[Risk]:
        statement = (
            select(RiskModel)
            .where(RiskModel.deleted_at.is_(None))
            .order_by(RiskModel.created_at.desc())
        )
        if organization_id:
            statement = statement.where(RiskModel.organization_id == organization_id)
        rows = self._session.scalars(statement).all()
        return [to_risk(row) for row in rows]

    def create(
        self,
        organization_id: UUID,
        title: str,
        description: str,
        severity: RiskSeverity,
        owner: str,
        created_by_id: UUID | None = None,
    ) -> Risk:
        model = RiskModel(
            organization_id=organization_id,
            title=title,
            description=description,
            severity=severity,
            status=RiskStatus.OPEN,
            owner=owner,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_risk(model)
