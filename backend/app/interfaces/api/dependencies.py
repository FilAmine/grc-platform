from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.application.use_cases import ControlService, OrganizationService, RiskService
from backend.app.infrastructure.database import get_db_session
from backend.app.infrastructure.repositories import (
    SqlAlchemyControlRepository,
    SqlAlchemyOrganizationRepository,
    SqlAlchemyRiskRepository,
)


def get_session() -> Generator[Session, None, None]:
    yield from get_db_session()


def get_organization_service(session: Session = Depends(get_session)) -> OrganizationService:
    return OrganizationService(SqlAlchemyOrganizationRepository(session))


def get_risk_service(session: Session = Depends(get_session)) -> RiskService:
    return RiskService(SqlAlchemyRiskRepository(session))


def get_control_service(session: Session = Depends(get_session)) -> ControlService:
    return ControlService(SqlAlchemyControlRepository(session))
