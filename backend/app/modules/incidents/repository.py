from datetime import datetime
from uuid import UUID

from backend.app.modules.incidents.models import IncidentModel
from backend.app.modules.incidents.service import Incident, IncidentSeverity, IncidentStatus
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_incident(model: IncidentModel) -> Incident:
    return Incident(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        description=model.description,
        severity=model.severity,
        status=model.status,
        reported_by=model.reported_by,
        resolved_at=model.resolved_at,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyIncidentRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Incident]:
        statement = (
            select(IncidentModel)
            .where(IncidentModel.deleted_at.is_(None))
            .where(IncidentModel.organization_id == organization_id)
            .order_by(IncidentModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_incident(row) for row in rows]

    def get_by_id(self, incident_id: UUID) -> Incident | None:
        model = self._session.get(IncidentModel, incident_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_incident(model)

    def create(
        self,
        organization_id: UUID,
        title: str,
        severity: IncidentSeverity,
        reported_by: str,
        description: str,
        created_by_id: UUID | None,
    ) -> Incident:
        model = IncidentModel(
            organization_id=organization_id,
            title=title,
            severity=severity,
            status=IncidentStatus.OPEN,
            reported_by=reported_by,
            description=description,
            resolved_at=None,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_incident(model)

    def set_status(
        self, incident_id: UUID, status: IncidentStatus, resolved_at: datetime | None
    ) -> Incident:
        model = self._session.get(IncidentModel, incident_id)
        assert model is not None
        model.status = status
        # Unconditional assignment (including None) -- unlike
        # AuditRepository.set_corrective_action_status's `if completed_at is
        # not None` guard, which never clears a previously-set timestamp.
        # Incidents' `reopen` transition (RESOLVED -> INVESTIGATING) actually
        # exercises the path back out of RESOLVED, so resolved_at must clear
        # too, or a reopened incident would incorrectly still show as resolved.
        model.resolved_at = resolved_at
        self._session.commit()
        self._session.refresh(model)
        return to_incident(model)
