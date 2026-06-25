from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.domain.entities import Control, Organization, Risk, RiskSeverity, RiskStatus
from backend.app.domain.repositories import ControlRepository, OrganizationRepository, RiskRepository
from backend.app.infrastructure.models import ControlModel, OrganizationModel, RiskModel


def to_organization(model: OrganizationModel) -> Organization:
    return Organization(
        id=model.id,
        name=model.name,
        slug=model.slug,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_risk(model: RiskModel) -> Risk:
    return Risk(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        description=model.description,
        severity=model.severity,
        status=model.status,
        owner=model.owner,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_control(model: ControlModel) -> Control:
    return Control(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        framework=model.framework,
        status=model.status,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyOrganizationRepository(OrganizationRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self) -> list[Organization]:
        rows = self._session.scalars(select(OrganizationModel).order_by(OrganizationModel.name)).all()
        return [to_organization(row) for row in rows]

    def create(self, name: str, slug: str) -> Organization:
        model = OrganizationModel(name=name, slug=slug)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_organization(model)


class SqlAlchemyRiskRepository(RiskRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID | None = None) -> list[Risk]:
        statement = select(RiskModel).order_by(RiskModel.created_at.desc())
        if organization_id:
            statement = statement.where(RiskModel.organization_id == organization_id)
        rows = self._session.scalars(statement).all()
        return [to_risk(row) for row in rows]

    def create(
        self,
        organization_id: UUID,
        title: str,
        description: str,
        severity: RiskSeverity,
        owner: str,
    ) -> Risk:
        model = RiskModel(
            organization_id=organization_id,
            title=title,
            description=description,
            severity=severity,
            status=RiskStatus.OPEN,
            owner=owner,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_risk(model)


class SqlAlchemyControlRepository(ControlRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID | None = None) -> list[Control]:
        statement = select(ControlModel).order_by(ControlModel.name)
        if organization_id:
            statement = statement.where(ControlModel.organization_id == organization_id)
        rows = self._session.scalars(statement).all()
        return [to_control(row) for row in rows]

    def create(
        self,
        organization_id: UUID,
        name: str,
        description: str,
        framework: str,
    ) -> Control:
        model = ControlModel(
            organization_id=organization_id,
            name=name,
            description=description,
            framework=framework,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_control(model)
