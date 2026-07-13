from uuid import UUID

from backend.app.modules.ecosystem_parties.models import EcosystemPartyModel
from backend.app.modules.ecosystem_parties.service import (
    EcosystemParty,
    EcosystemPartyCategory,
    EcosystemPartyLevel,
)
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_ecosystem_party(model: EcosystemPartyModel) -> EcosystemParty:
    return EcosystemParty(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        category=model.category,
        dependency_level=model.dependency_level,
        cyber_maturity=model.cyber_maturity,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyEcosystemPartyRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[EcosystemParty]:
        statement = (
            select(EcosystemPartyModel)
            .where(EcosystemPartyModel.deleted_at.is_(None))
            .where(EcosystemPartyModel.organization_id == organization_id)
            .order_by(EcosystemPartyModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_ecosystem_party(row) for row in rows]

    def get_by_id(self, ecosystem_party_id: UUID) -> EcosystemParty | None:
        model = self._session.get(EcosystemPartyModel, ecosystem_party_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_ecosystem_party(model)

    def create(
        self,
        organization_id: UUID,
        name: str,
        category: EcosystemPartyCategory,
        description: str,
        dependency_level: EcosystemPartyLevel,
        cyber_maturity: EcosystemPartyLevel,
        created_by_id: UUID | None,
    ) -> EcosystemParty:
        model = EcosystemPartyModel(
            organization_id=organization_id,
            name=name,
            category=category,
            description=description,
            dependency_level=dependency_level,
            cyber_maturity=cyber_maturity,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_ecosystem_party(model)
