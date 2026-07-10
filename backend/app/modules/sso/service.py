from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class SsoConnection:
    id: UUID
    organization_id: UUID
    issuer: str
    client_id: str
    # Present on the domain object (needed server-side for the token exchange)
    # but deliberately absent from schemas.SsoConnectionRead, so it's never
    # serialized back to the client -- same pattern as User.hashed_password.
    client_secret: str
    default_role_id: UUID | None
    is_enabled: bool
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class ConfigureSsoCommand:
    organization_id: UUID
    issuer: str
    client_id: str
    client_secret: str
    default_role_id: UUID | None
    is_enabled: bool
    actor_id: UUID | None = None


class SsoConnectionStore(Protocol):
    def get_by_organization(self, organization_id: UUID) -> SsoConnection | None:
        raise NotImplementedError

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
        raise NotImplementedError

    def delete(self, organization_id: UUID) -> None:
        raise NotImplementedError


class SsoService:
    def __init__(self, connections: SsoConnectionStore) -> None:
        self._connections = connections

    def get_connection(self, organization_id: UUID) -> SsoConnection | None:
        return self._connections.get_by_organization(organization_id)

    def configure(self, command: ConfigureSsoCommand) -> SsoConnection:
        return self._connections.upsert(
            organization_id=command.organization_id,
            issuer=command.issuer,
            client_id=command.client_id,
            client_secret=command.client_secret,
            default_role_id=command.default_role_id,
            is_enabled=command.is_enabled,
            actor_id=command.actor_id,
        )

    def remove(self, organization_id: UUID) -> None:
        self._connections.delete(organization_id)
