from uuid import UUID

from backend.app.modules.strategic_scenarios.models import StrategicScenarioModel
from backend.app.modules.strategic_scenarios.service import StrategicScenario, StrategicScenarioLikelihood
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_strategic_scenario(model: StrategicScenarioModel) -> StrategicScenario:
    return StrategicScenario(
        id=model.id,
        organization_id=model.organization_id,
        risk_origin_id=model.risk_origin_id,
        feared_event_id=model.feared_event_id,
        ecosystem_party_id=model.ecosystem_party_id,
        name=model.name,
        description=model.description,
        likelihood=model.likelihood,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyStrategicScenarioRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[StrategicScenario]:
        statement = (
            select(StrategicScenarioModel)
            .where(StrategicScenarioModel.deleted_at.is_(None))
            .where(StrategicScenarioModel.organization_id == organization_id)
            .order_by(StrategicScenarioModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_strategic_scenario(row) for row in rows]

    def get_by_id(self, strategic_scenario_id: UUID) -> StrategicScenario | None:
        model = self._session.get(StrategicScenarioModel, strategic_scenario_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_strategic_scenario(model)

    def create(
        self,
        organization_id: UUID,
        risk_origin_id: UUID,
        feared_event_id: UUID,
        name: str,
        ecosystem_party_id: UUID | None,
        description: str,
        likelihood: StrategicScenarioLikelihood,
        created_by_id: UUID | None,
    ) -> StrategicScenario:
        model = StrategicScenarioModel(
            organization_id=organization_id,
            risk_origin_id=risk_origin_id,
            feared_event_id=feared_event_id,
            ecosystem_party_id=ecosystem_party_id,
            name=name,
            description=description,
            likelihood=likelihood,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_strategic_scenario(model)
