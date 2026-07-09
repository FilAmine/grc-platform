from __future__ import annotations

from datetime import date, datetime
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.modules.audits.models import (
    AuditModel,
    ChecklistItemModel,
    CorrectiveActionModel,
    FindingModel,
)
from backend.app.modules.audits.service import (
    Audit,
    AuditStatus,
    ChecklistItem,
    ChecklistItemStatus,
    CorrectiveAction,
    CorrectiveActionStatus,
    Finding,
    FindingSeverity,
    FindingStatus,
)


def to_audit(model: AuditModel) -> Audit:
    return Audit(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        scope=model.scope,
        lead_auditor=model.lead_auditor,
        status=model.status,
        period_start=model.period_start,
        period_end=model.period_end,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_checklist_item(model: ChecklistItemModel) -> ChecklistItem:
    return ChecklistItem(
        id=model.id,
        audit_id=model.audit_id,
        description=model.description,
        status=model.status,
        notes=model.notes,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_finding(model: FindingModel) -> Finding:
    return Finding(
        id=model.id,
        audit_id=model.audit_id,
        checklist_item_id=model.checklist_item_id,
        title=model.title,
        description=model.description,
        severity=model.severity,
        status=model.status,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_corrective_action(model: CorrectiveActionModel) -> CorrectiveAction:
    return CorrectiveAction(
        id=model.id,
        finding_id=model.finding_id,
        description=model.description,
        owner=model.owner,
        due_date=model.due_date,
        status=model.status,
        completed_at=model.completed_at,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyAuditRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Audit]:
        statement = (
            select(AuditModel)
            .where(AuditModel.organization_id == organization_id, AuditModel.deleted_at.is_(None))
            .order_by(AuditModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_audit(row) for row in rows]

    def get_by_id(self, audit_id: UUID) -> Audit | None:
        model = self._session.get(AuditModel, audit_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_audit(model)

    def create(
        self,
        organization_id: UUID,
        title: str,
        scope: str,
        lead_auditor: str,
        period_start: date | None,
        period_end: date | None,
        created_by_id: UUID | None,
    ) -> Audit:
        model = AuditModel(
            organization_id=organization_id,
            title=title,
            scope=scope,
            lead_auditor=lead_auditor,
            period_start=period_start,
            period_end=period_end,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_audit(model)

    def set_status(self, audit_id: UUID, status: AuditStatus) -> Audit:
        model = self._session.get(AuditModel, audit_id)
        if model is None:
            raise ValueError("audit not found")
        model.status = status
        self._session.commit()
        self._session.refresh(model)
        return to_audit(model)

    def add_checklist_item(self, audit_id: UUID, description: str) -> ChecklistItem:
        model = ChecklistItemModel(audit_id=audit_id, description=description)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_checklist_item(model)

    def list_checklist_items(self, audit_id: UUID) -> list[ChecklistItem]:
        statement = select(ChecklistItemModel).where(ChecklistItemModel.audit_id == audit_id)
        rows = self._session.scalars(statement).all()
        return [to_checklist_item(row) for row in rows]

    def set_checklist_item_status(
        self, item_id: UUID, status: ChecklistItemStatus, notes: str
    ) -> ChecklistItem:
        model = self._session.get(ChecklistItemModel, item_id)
        if model is None:
            raise ValueError("checklist item not found")
        model.status = status
        model.notes = notes
        self._session.commit()
        self._session.refresh(model)
        return to_checklist_item(model)

    def add_finding(
        self,
        audit_id: UUID,
        title: str,
        description: str,
        severity: FindingSeverity,
        checklist_item_id: UUID | None,
    ) -> Finding:
        model = FindingModel(
            audit_id=audit_id,
            title=title,
            description=description,
            severity=severity,
            checklist_item_id=checklist_item_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_finding(model)

    def list_findings(self, audit_id: UUID) -> list[Finding]:
        statement = select(FindingModel).where(FindingModel.audit_id == audit_id)
        rows = self._session.scalars(statement).all()
        return [to_finding(row) for row in rows]

    def get_finding(self, finding_id: UUID) -> Finding | None:
        model = self._session.get(FindingModel, finding_id)
        return to_finding(model) if model else None

    def set_finding_status(self, finding_id: UUID, status: FindingStatus) -> Finding:
        model = self._session.get(FindingModel, finding_id)
        if model is None:
            raise ValueError("finding not found")
        model.status = status
        self._session.commit()
        self._session.refresh(model)
        return to_finding(model)

    def add_corrective_action(
        self, finding_id: UUID, description: str, owner: str, due_date: date | None
    ) -> CorrectiveAction:
        model = CorrectiveActionModel(
            finding_id=finding_id, description=description, owner=owner, due_date=due_date
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_corrective_action(model)

    def list_corrective_actions(self, finding_id: UUID) -> list[CorrectiveAction]:
        statement = select(CorrectiveActionModel).where(CorrectiveActionModel.finding_id == finding_id)
        rows = self._session.scalars(statement).all()
        return [to_corrective_action(row) for row in rows]

    def set_corrective_action_status(
        self, action_id: UUID, status: CorrectiveActionStatus, completed_at: datetime | None
    ) -> CorrectiveAction:
        model = self._session.get(CorrectiveActionModel, action_id)
        if model is None:
            raise ValueError("corrective action not found")
        model.status = status
        if completed_at is not None:
            model.completed_at = completed_at
        self._session.commit()
        self._session.refresh(model)
        return to_corrective_action(model)
