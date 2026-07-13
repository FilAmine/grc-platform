from uuid import UUID

from backend.app.modules.risk_origins.models import RiskOriginModel
from backend.app.modules.risk_origins.service import RiskOrigin, RiskOriginPertinence
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_risk_origin(model: RiskOriginModel) -> RiskOrigin:
    return RiskOrigin(
        id=model.id,
        organization_id=model.organization_id,
        risk_source_id=model.risk_source_id,
        target_objective=model.target_objective,
        feared_event_id=model.feared_event_id,
        pertinence=model.pertinence,
        retained=model.retained,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyRiskOriginRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[RiskOrigin]:
        statement = (
            select(RiskOriginModel)
            .where(RiskOriginModel.deleted_at.is_(None))
            .where(RiskOriginModel.organization_id == organization_id)
            .order_by(RiskOriginModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_risk_origin(row) for row in rows]

    def get_by_id(self, risk_origin_id: UUID) -> RiskOrigin | None:
        model = self._session.get(RiskOriginModel, risk_origin_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_risk_origin(model)

    def create(
        self,
        organization_id: UUID,
        risk_source_id: UUID,
        target_objective: str,
        feared_event_id: UUID | None,
        pertinence: RiskOriginPertinence,
        retained: bool,
        created_by_id: UUID | None,
    ) -> RiskOrigin:
        model = RiskOriginModel(
            organization_id=organization_id,
            risk_source_id=risk_source_id,
            target_objective=target_objective,
            feared_event_id=feared_event_id,
            pertinence=pertinence,
            retained=retained,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_risk_origin(model)
