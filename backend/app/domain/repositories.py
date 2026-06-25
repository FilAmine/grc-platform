from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.domain.entities import Control, Organization, Risk, RiskSeverity


class OrganizationRepository(ABC):
    @abstractmethod
    def list(self) -> list[Organization]:
        raise NotImplementedError

    @abstractmethod
    def create(self, name: str, slug: str) -> Organization:
        raise NotImplementedError


class RiskRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID | None = None) -> list[Risk]:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        title: str,
        description: str,
        severity: RiskSeverity,
        owner: str,
    ) -> Risk:
        raise NotImplementedError


class ControlRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID | None = None) -> list[Control]:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        framework: str,
    ) -> Control:
        raise NotImplementedError
