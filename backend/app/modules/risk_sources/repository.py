from uuid import UUID

from backend.app.modules.risk_sources.models import RiskSourceModel
from backend.app.modules.risk_sources.service import (
    RiskSource,
    RiskSourceActivity,
    RiskSourceCategory,
    RiskSourceLevel,
)
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_risk_source(model: RiskSourceModel) -> RiskSource:
    return RiskSource(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        category=model.category,
        motivation=model.motivation,
        resources=model.resources,
        activity=model.activity,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyRiskSourceRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[RiskSource]:
        statement = (
            select(RiskSourceModel)
            .where(RiskSourceModel.deleted_at.is_(None))
            .where(RiskSourceModel.organization_id == organization_id)
            .order_by(RiskSourceModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_risk_source(row) for row in rows]

    def get_by_id(self, risk_source_id: UUID) -> RiskSource | None:
        model = self._session.get(RiskSourceModel, risk_source_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_risk_source(model)

    def create(
        self,
        organization_id: UUID,
        name: str,
        category: RiskSourceCategory,
        description: str,
        motivation: RiskSourceLevel,
        resources: RiskSourceLevel,
        activity: RiskSourceActivity,
        created_by_id: UUID | None,
    ) -> RiskSource:
        model = RiskSourceModel(
            organization_id=organization_id,
            name=name,
            category=category,
            description=description,
            motivation=motivation,
            resources=resources,
            activity=activity,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_risk_source(model)
