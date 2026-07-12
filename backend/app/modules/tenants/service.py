from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class Tenant:
    id: UUID
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateTenantCommand:
    name: str
    slug: str


class TenantStore(Protocol):
    def list(self) -> list[Tenant]:
        raise NotImplementedError

    def get_by_id(self, tenant_id: UUID) -> Tenant | None:
        raise NotImplementedError

    def create(self, name: str, slug: str) -> Tenant:
        raise NotImplementedError


class TenantService:
    def __init__(self, tenants: TenantStore) -> None:
        self._tenants = tenants

    def list_tenants(self) -> list[Tenant]:
        return self._tenants.list()

    def get_tenant(self, tenant_id: UUID) -> Tenant | None:
        return self._tenants.get_by_id(tenant_id)

    def create_tenant(self, command: CreateTenantCommand) -> Tenant:
        return self._tenants.create(name=command.name, slug=command.slug)
