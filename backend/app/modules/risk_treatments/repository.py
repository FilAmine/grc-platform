from uuid import UUID

from backend.app.modules.risk_treatments.models import RiskTreatmentModel
from backend.app.modules.risk_treatments.service import (
    RiskTreatment,
    RiskTreatmentDecision,
    RiskTreatmentResidualRisk,
)
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_risk_treatment(model: RiskTreatmentModel) -> RiskTreatment:
    return RiskTreatment(
        id=model.id,
        organization_id=model.organization_id,
        strategic_scenario_id=model.strategic_scenario_id,
        decision=model.decision,
        justification=model.justification,
        residual_risk_level=model.residual_risk_level,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyRiskTreatmentRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[RiskTreatment]:
        statement = (
            select(RiskTreatmentModel)
            .where(RiskTreatmentModel.deleted_at.is_(None))
            .where(RiskTreatmentModel.organization_id == organization_id)
            .order_by(RiskTreatmentModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_risk_treatment(row) for row in rows]

    def get_by_id(self, risk_treatment_id: UUID) -> RiskTreatment | None:
        model = self._session.get(RiskTreatmentModel, risk_treatment_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_risk_treatment(model)

    def create(
        self,
        organization_id: UUID,
        strategic_scenario_id: UUID,
        decision: RiskTreatmentDecision,
        justification: str,
        residual_risk_level: RiskTreatmentResidualRisk,
        created_by_id: UUID | None,
    ) -> RiskTreatment:
        model = RiskTreatmentModel(
            organization_id=organization_id,
            strategic_scenario_id=strategic_scenario_id,
            decision=decision,
            justification=justification,
            residual_risk_level=residual_risk_level,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_risk_treatment(model)
