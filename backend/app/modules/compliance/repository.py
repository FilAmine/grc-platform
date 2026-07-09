from typing import Protocol

from backend.app.modules.controls.service import Control
from backend.app.modules.organizations.service import Organization
from backend.app.modules.risks.service import Risk


class OrganizationReader(Protocol):
    def list_organizations(self) -> list[Organization]:
        raise NotImplementedError


class RiskReader(Protocol):
    def list_risks(self) -> list[Risk]:
        raise NotImplementedError


class ControlReader(Protocol):
    def list_controls(self) -> list[Control]:
        raise NotImplementedError
