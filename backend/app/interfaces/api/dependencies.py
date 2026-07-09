from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.database import get_db_session
from backend.app.modules.compliance.service import ComplianceService
from backend.app.modules.controls.repository import (
    SqlAlchemyControlRepository,
)
from backend.app.modules.controls.service import ControlService
from backend.app.modules.dashboard.service import DashboardService
from backend.app.modules.organizations.repository import (
    SqlAlchemyOrganizationRepository,
)
from backend.app.modules.organizations.service import OrganizationService
from backend.app.modules.risks.repository import (
    SqlAlchemyRiskRepository,
)
from backend.app.modules.risks.service import RiskService


def get_session() -> Generator[Session, None, None]:
    yield from get_db_session()


def get_organization_service(session: Session = Depends(get_session)) -> OrganizationService:
    return OrganizationService(SqlAlchemyOrganizationRepository(session))


def get_risk_service(session: Session = Depends(get_session)) -> RiskService:
    return RiskService(SqlAlchemyRiskRepository(session))


def get_control_service(session: Session = Depends(get_session)) -> ControlService:
    return ControlService(SqlAlchemyControlRepository(session))


def get_compliance_service(session: Session = Depends(get_session)) -> ComplianceService:
    organizations = OrganizationService(SqlAlchemyOrganizationRepository(session))
    risks = RiskService(SqlAlchemyRiskRepository(session))
    controls = ControlService(SqlAlchemyControlRepository(session))
    return ComplianceService(organizations=organizations, risks=risks, controls=controls)


def get_dashboard_service(
    compliance: ComplianceService = Depends(get_compliance_service),
) -> DashboardService:
    return DashboardService(compliance)
