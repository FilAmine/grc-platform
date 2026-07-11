from uuid import UUID

from backend.app.modules.feared_events.models import FearedEventModel
from backend.app.modules.feared_events.service import (
    FearedEvent,
    FearedEventCriterion,
    FearedEventGravity,
)
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_feared_event(model: FearedEventModel) -> FearedEvent:
    return FearedEvent(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        description=model.description,
        asset_id=model.asset_id,
        criterion=model.criterion,
        gravity=model.gravity,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyFearedEventRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[FearedEvent]:
        statement = (
            select(FearedEventModel)
            .where(FearedEventModel.deleted_at.is_(None))
            .where(FearedEventModel.organization_id == organization_id)
            .order_by(FearedEventModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_feared_event(row) for row in rows]

    def get_by_id(self, feared_event_id: UUID) -> FearedEvent | None:
        model = self._session.get(FearedEventModel, feared_event_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_feared_event(model)

    def create(
        self,
        organization_id: UUID,
        title: str,
        asset_id: UUID,
        criterion: FearedEventCriterion,
        gravity: FearedEventGravity,
        description: str,
        created_by_id: UUID | None,
    ) -> FearedEvent:
        model = FearedEventModel(
            organization_id=organization_id,
            title=title,
            asset_id=asset_id,
            criterion=criterion,
            gravity=gravity,
            description=description,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_feared_event(model)
