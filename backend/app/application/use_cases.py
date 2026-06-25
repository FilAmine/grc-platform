from dataclasses import dataclass
from uuid import UUID

from backend.app.domain.entities import Control, Organization, Risk, RiskSeverity
from backend.app.domain.repositories import ControlRepository, OrganizationRepository, RiskRepository


@dataclass(frozen=True)
class CreateOrganizationCommand:
    name: str
    slug: str


@dataclass(frozen=True)
class CreateRiskCommand:
    organization_id: UUID
    title: str
    description: str
    severity: RiskSeverity
    owner: str


@dataclass(frozen=True)
class CreateControlCommand:
    organization_id: UUID
    name: str
    description: str
    framework: str


class OrganizationService:
    def __init__(self, organizations: OrganizationRepository) -> None:
        self._organizations = organizations

    def list_organizations(self) -> list[Organization]:
        return self._organizations.list()

    def create_organization(self, command: CreateOrganizationCommand) -> Organization:
        return self._organizations.create(name=command.name, slug=command.slug)


class RiskService:
    def __init__(self, risks: RiskRepository) -> None:
        self._risks = risks

    def list_risks(self, organization_id: UUID | None = None) -> list[Risk]:
        return self._risks.list(organization_id=organization_id)

    def create_risk(self, command: CreateRiskCommand) -> Risk:
        return self._risks.create(
            organization_id=command.organization_id,
            title=command.title,
            description=command.description,
            severity=command.severity,
            owner=command.owner,
        )


class ControlService:
    def __init__(self, controls: ControlRepository) -> None:
        self._controls = controls

    def list_controls(self, organization_id: UUID | None = None) -> list[Control]:
        return self._controls.list(organization_id=organization_id)

    def create_control(self, command: CreateControlCommand) -> Control:
        return self._controls.create(
            organization_id=command.organization_id,
            name=command.name,
            description=command.description,
            framework=command.framework,
        )
