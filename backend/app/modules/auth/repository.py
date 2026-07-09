from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from backend.app.modules.auth.models import RefreshTokenModel
from sqlalchemy import select
from sqlalchemy.orm import Session


class RefreshTokenRepository(ABC):
    @abstractmethod
    def create(self, user_id: UUID, token_hash: str, expires_at: datetime) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_active_by_hash(self, token_hash: str, now: datetime) -> RefreshTokenModel | None:
        raise NotImplementedError

    @abstractmethod
    def revoke(self, token_id: UUID, now: datetime) -> None:
        raise NotImplementedError

    @abstractmethod
    def revoke_all_for_user(self, user_id: UUID, now: datetime) -> None:
        raise NotImplementedError


class SqlAlchemyRefreshTokenRepository(RefreshTokenRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, user_id: UUID, token_hash: str, expires_at: datetime) -> None:
        model = RefreshTokenModel(user_id=user_id, token_hash=token_hash, expires_at=expires_at)
        self._session.add(model)
        self._session.commit()

    def get_active_by_hash(self, token_hash: str, now: datetime) -> RefreshTokenModel | None:
        statement = select(RefreshTokenModel).where(
            RefreshTokenModel.token_hash == token_hash,
            RefreshTokenModel.revoked_at.is_(None),
            RefreshTokenModel.expires_at > now,
        )
        return self._session.scalars(statement).first()

    def revoke(self, token_id: UUID, now: datetime) -> None:
        model = self._session.get(RefreshTokenModel, token_id)
        if model is not None:
            model.revoked_at = now
            self._session.commit()

    def revoke_all_for_user(self, user_id: UUID, now: datetime) -> None:
        statement = select(RefreshTokenModel).where(
            RefreshTokenModel.user_id == user_id, RefreshTokenModel.revoked_at.is_(None)
        )
        for model in self._session.scalars(statement).all():
            model.revoked_at = now
        self._session.commit()
