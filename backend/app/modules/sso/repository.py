from uuid import UUID

from backend.app.modules.sso.models import SsoConnectionModel
from backend.app.modules.sso.service import SsoConnection
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_sso_connection(model: SsoConnectionModel) -> SsoConnection:
    return SsoConnection(
        id=model.id,
        organization_id=model.organization_id,
        issuer=model.issuer,
        client_id=model.client_id,
        client_secret=model.client_secret,
        default_role_id=model.default_role_id,
        is_enabled=model.is_enabled,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemySsoConnectionRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_organization(self, organization_id: UUID) -> SsoConnection | None:
        statement = select(SsoConnectionModel).where(SsoConnectionModel.organization_id == organization_id)
        model = self._session.scalars(statement).first()
        return to_sso_connection(model) if model else None

    def upsert(
        self,
        organization_id: UUID,
        issuer: str,
        client_id: str,
        client_secret: str,
        default_role_id: UUID | None,
        is_enabled: bool,
        actor_id: UUID | None,
    ) -> SsoConnection:
        statement = select(SsoConnectionModel).where(SsoConnectionModel.organization_id == organization_id)
        model = self._session.scalars(statement).first()
        if model is None:
            model = SsoConnectionModel(organization_id=organization_id, created_by_id=actor_id)
            self._session.add(model)
        model.issuer = issuer
        model.client_id = client_id
        model.client_secret = client_secret
        model.default_role_id = default_role_id
        model.is_enabled = is_enabled
        model.updated_by_id = actor_id
        self._session.commit()
        self._session.refresh(model)
        return to_sso_connection(model)

    def delete(self, organization_id: UUID) -> None:
        statement = select(SsoConnectionModel).where(SsoConnectionModel.organization_id == organization_id)
        model = self._session.scalars(statement).first()
        if model is not None:
            self._session.delete(model)
            self._session.commit()
