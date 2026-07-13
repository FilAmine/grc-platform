# Same `list`-method-shadows-builtin-`list` issue as service.py -- see that
# file's comment.
from __future__ import annotations

from uuid import UUID

from backend.app.modules.operational_scenarios.models import OperationalScenarioModel
from backend.app.modules.operational_scenarios.service import (
    OperationalScenario,
    OperationalScenarioLikelihood,
)
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_operational_scenario(model: OperationalScenarioModel) -> OperationalScenario:
    return OperationalScenario(
        id=model.id,
        organization_id=model.organization_id,
        strategic_scenario_id=model.strategic_scenario_id,
        name=model.name,
        description=model.description,
        mitre_technique_ids=list(model.mitre_technique_ids),
        technical_likelihood=model.technical_likelihood,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyOperationalScenarioRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[OperationalScenario]:
        statement = (
            select(OperationalScenarioModel)
            .where(OperationalScenarioModel.deleted_at.is_(None))
            .where(OperationalScenarioModel.organization_id == organization_id)
            .order_by(OperationalScenarioModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_operational_scenario(row) for row in rows]

    def get_by_id(self, operational_scenario_id: UUID) -> OperationalScenario | None:
        model = self._session.get(OperationalScenarioModel, operational_scenario_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_operational_scenario(model)

    def create(
        self,
        organization_id: UUID,
        strategic_scenario_id: UUID,
        name: str,
        description: str,
        mitre_technique_ids: list[str],
        technical_likelihood: OperationalScenarioLikelihood,
        created_by_id: UUID | None,
    ) -> OperationalScenario:
        model = OperationalScenarioModel(
            organization_id=organization_id,
            strategic_scenario_id=strategic_scenario_id,
            name=name,
            description=description,
            mitre_technique_ids=mitre_technique_ids,
            technical_likelihood=technical_likelihood,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_operational_scenario(model)
