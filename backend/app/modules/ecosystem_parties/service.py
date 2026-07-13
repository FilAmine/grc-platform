"""EBIOS RM Workshop 3's ecosystem cartography: third parties (suppliers,
subcontractors, partners, clients) that a strategic scenario's attack path
can use as a stepping stone to reach the organization -- ANSSI's methodology
treats "attack via the ecosystem" as a first-class case, not an edge case.
"""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID


class EcosystemPartyCategory(StrEnum):
    PROVIDER = "provider"
    SUBCONTRACTOR = "subcontractor"
    PARTNER = "partner"
    CLIENT = "client"


class EcosystemPartyLevel(StrEnum):
    """Shared 3-level scale for both dependency and cyber-maturity scoring."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class EcosystemParty:
    id: UUID
    organization_id: UUID
    name: str
    description: str
    category: EcosystemPartyCategory
    # How critical this party is to the organization's own operations --
    # not how risky they are as an attack vector (that's cyber_maturity,
    # inverted: LOW maturity = a more attractive stepping stone).
    dependency_level: EcosystemPartyLevel
    cyber_maturity: EcosystemPartyLevel
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateEcosystemPartyCommand:
    organization_id: UUID
    name: str
    category: EcosystemPartyCategory
    description: str = ""
    dependency_level: EcosystemPartyLevel = EcosystemPartyLevel.MEDIUM
    cyber_maturity: EcosystemPartyLevel = EcosystemPartyLevel.MEDIUM
    created_by_id: UUID | None = None


class EcosystemPartyStore(Protocol):
    def list(self, organization_id: UUID) -> list[EcosystemParty]:
        raise NotImplementedError

    def get_by_id(self, ecosystem_party_id: UUID) -> EcosystemParty | None:
        raise NotImplementedError

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
        raise NotImplementedError


class EcosystemPartyService:
    def __init__(self, ecosystem_parties: EcosystemPartyStore) -> None:
        self._ecosystem_parties = ecosystem_parties

    def list_ecosystem_parties(self, organization_id: UUID) -> list[EcosystemParty]:
        return self._ecosystem_parties.list(organization_id)

    def get_ecosystem_party(self, ecosystem_party_id: UUID) -> EcosystemParty | None:
        return self._ecosystem_parties.get_by_id(ecosystem_party_id)

    def create_ecosystem_party(self, command: CreateEcosystemPartyCommand) -> EcosystemParty:
        return self._ecosystem_parties.create(
            organization_id=command.organization_id,
            name=command.name,
            category=command.category,
            description=command.description,
            dependency_level=command.dependency_level,
            cyber_maturity=command.cyber_maturity,
            created_by_id=command.created_by_id,
        )
