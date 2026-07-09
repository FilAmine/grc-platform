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


@dataclass(frozen=True)
class CreateOrganizationCommand:
    name: str
    slug: str


class OrganizationStore(Protocol):
    def list(self) -> list[Organization]:
        raise NotImplementedError

    def create(self, name: str, slug: str) -> Organization:
        raise NotImplementedError


class OrganizationService:
    def __init__(self, organizations: OrganizationStore) -> None:
        self._organizations = organizations

    def list_organizations(self) -> list[Organization]:
        return self._organizations.list()

    def create_organization(self, command: CreateOrganizationCommand) -> Organization:
        return self._organizations.create(name=command.name, slug=command.slug)
