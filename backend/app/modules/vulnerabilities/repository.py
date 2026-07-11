from abc import ABC, abstractmethod
from uuid import UUID

from backend.app.modules.vulnerabilities.models import VulnerabilityModel
from backend.app.modules.vulnerabilities.service import (
    Vulnerability,
    VulnerabilitySeverity,
    VulnerabilityStatus,
)
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_vulnerability(model: VulnerabilityModel) -> Vulnerability:
    return Vulnerability(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        description=model.description,
        severity=model.severity,
        status=model.status,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class VulnerabilityRepository(ABC):
    @abstractmethod
    def list(self, organization_id: UUID) -> list[Vulnerability]:
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        organization_id: UUID,
        name: str,
        severity: VulnerabilitySeverity,
        description: str,
        created_by_id: UUID | None,
    ) -> Vulnerability:
        raise NotImplementedError


class SqlAlchemyVulnerabilityRepository(VulnerabilityRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Vulnerability]:
        statement = (
            select(VulnerabilityModel)
            .where(VulnerabilityModel.deleted_at.is_(None))
            .where(VulnerabilityModel.organization_id == organization_id)
            .order_by(VulnerabilityModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_vulnerability(row) for row in rows]

    def create(
        self,
        organization_id: UUID,
        name: str,
        severity: VulnerabilitySeverity,
        description: str,
        created_by_id: UUID | None,
    ) -> Vulnerability:
        model = VulnerabilityModel(
            organization_id=organization_id,
            name=name,
            severity=severity,
            description=description,
            status=VulnerabilityStatus.OPEN,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_vulnerability(model)
