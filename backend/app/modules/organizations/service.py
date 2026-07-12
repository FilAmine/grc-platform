from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class Organization:
    id: UUID
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    tenant_id: UUID | None = None


@dataclass(frozen=True)
class CreateOrganizationCommand:
    name: str
    slug: str


class OrganizationStore(Protocol):
    def list(self) -> list[Organization]:
        raise NotImplementedError

    def get_by_id(self, organization_id: UUID) -> Organization | None:
        raise NotImplementedError

    def get_by_slug(self, slug: str) -> Organization | None:
        raise NotImplementedError

    def create(self, name: str, slug: str) -> Organization:
        raise NotImplementedError

    def set_tenant(self, organization_id: UUID, tenant_id: UUID | None) -> Organization:
        raise NotImplementedError


class OrganizationService:
    def __init__(self, organizations: OrganizationStore) -> None:
        self._organizations = organizations

    def list_organizations(self) -> list[Organization]:
        return self._organizations.list()

    def get_organization(self, organization_id: UUID) -> Organization | None:
        return self._organizations.get_by_id(organization_id)

    def get_organization_by_slug(self, slug: str) -> Organization | None:
        return self._organizations.get_by_slug(slug)

    def create_organization(self, command: CreateOrganizationCommand) -> Organization:
        return self._organizations.create(name=command.name, slug=command.slug)

    def set_tenant(self, organization_id: UUID, tenant_id: UUID | None) -> Organization:
        return self._organizations.set_tenant(organization_id, tenant_id)
