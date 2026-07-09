from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID

from backend.app.workflow.state_machine import StateMachine, Transition


class AuditStatus(StrEnum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CLOSED = "closed"


AUDIT_STATUS_MACHINE: StateMachine[AuditStatus] = StateMachine(
    [
        Transition("start", AuditStatus.PLANNED, AuditStatus.IN_PROGRESS),
        Transition("complete", AuditStatus.IN_PROGRESS, AuditStatus.COMPLETED),
        Transition("close", AuditStatus.COMPLETED, AuditStatus.CLOSED),
        Transition("reopen", AuditStatus.COMPLETED, AuditStatus.IN_PROGRESS),
    ]
)


class ChecklistItemStatus(StrEnum):
    PENDING = "pending"
    DONE = "done"
    NOT_APPLICABLE = "not_applicable"


class FindingSeverity(StrEnum):
    MINOR = "minor"
    MAJOR = "major"
    CRITICAL = "critical"


class FindingStatus(StrEnum):
    OPEN = "open"
    IN_REMEDIATION = "in_remediation"
    CLOSED = "closed"


class CorrectiveActionStatus(StrEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass(frozen=True)
class Audit:
    id: UUID
    organization_id: UUID
    title: str
    scope: str
    lead_auditor: str
    status: AuditStatus
    period_start: date | None
    period_end: date | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class ChecklistItem:
    id: UUID
    audit_id: UUID
    description: str
    status: ChecklistItemStatus
    notes: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class Finding:
    id: UUID
    audit_id: UUID
    checklist_item_id: UUID | None
    title: str
    description: str
    severity: FindingSeverity
    status: FindingStatus
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CorrectiveAction:
    id: UUID
    finding_id: UUID
    description: str
    owner: str
    due_date: date | None
    status: CorrectiveActionStatus
    completed_at: datetime | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateAuditCommand:
    organization_id: UUID
    title: str
    scope: str
    lead_auditor: str
    period_start: date | None = None
    period_end: date | None = None
    created_by_id: UUID | None = None


@dataclass(frozen=True)
class CreateChecklistItemCommand:
    audit_id: UUID
    description: str


@dataclass(frozen=True)
class CreateFindingCommand:
    audit_id: UUID
    title: str
    description: str
    severity: FindingSeverity
    checklist_item_id: UUID | None = None


@dataclass(frozen=True)
class CreateCorrectiveActionCommand:
    finding_id: UUID
    description: str
    owner: str
    due_date: date | None = None


class AuditStore(Protocol):
    def list(self, organization_id: UUID) -> list[Audit]:
        raise NotImplementedError

    def get_by_id(self, audit_id: UUID) -> Audit | None:
        raise NotImplementedError

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
        raise NotImplementedError

    def set_status(self, audit_id: UUID, status: AuditStatus) -> Audit:
        raise NotImplementedError

    def add_checklist_item(self, audit_id: UUID, description: str) -> ChecklistItem:
        raise NotImplementedError

    def list_checklist_items(self, audit_id: UUID) -> list[ChecklistItem]:
        raise NotImplementedError

    def set_checklist_item_status(
        self, item_id: UUID, status: ChecklistItemStatus, notes: str
    ) -> ChecklistItem:
        raise NotImplementedError

    def add_finding(
        self,
        audit_id: UUID,
        title: str,
        description: str,
        severity: FindingSeverity,
        checklist_item_id: UUID | None,
    ) -> Finding:
        raise NotImplementedError

    def list_findings(self, audit_id: UUID) -> list[Finding]:
        raise NotImplementedError

    def set_finding_status(self, finding_id: UUID, status: FindingStatus) -> Finding:
        raise NotImplementedError

    def get_finding(self, finding_id: UUID) -> Finding | None:
        raise NotImplementedError

    def add_corrective_action(
        self, finding_id: UUID, description: str, owner: str, due_date: date | None
    ) -> CorrectiveAction:
        raise NotImplementedError

    def list_corrective_actions(self, finding_id: UUID) -> list[CorrectiveAction]:
        raise NotImplementedError

    def set_corrective_action_status(
        self, action_id: UUID, status: CorrectiveActionStatus, completed_at: datetime | None
    ) -> CorrectiveAction:
        raise NotImplementedError


class AuditNotFoundError(Exception):
    pass


@dataclass(frozen=True)
class AuditReport:
    audit: Audit
    checklist_total: int
    checklist_done: int
    findings_by_severity: dict[str, int]
    open_findings: int
    corrective_actions_total: int
    corrective_actions_done: int


class AuditService:
    def __init__(self, audits: AuditStore) -> None:
        self._audits = audits

    def list_audits(self, organization_id: UUID) -> list[Audit]:
        return self._audits.list(organization_id)

    def get_audit(self, audit_id: UUID) -> Audit | None:
        return self._audits.get_by_id(audit_id)

    def get_finding(self, finding_id: UUID) -> Finding | None:
        return self._audits.get_finding(finding_id)

    def create_audit(self, command: CreateAuditCommand) -> Audit:
        return self._audits.create(
            organization_id=command.organization_id,
            title=command.title,
            scope=command.scope,
            lead_auditor=command.lead_auditor,
            period_start=command.period_start,
            period_end=command.period_end,
            created_by_id=command.created_by_id,
        )

    def set_status(self, audit_id: UUID, status: AuditStatus) -> Audit:
        current = self._audits.get_by_id(audit_id)
        if current is None:
            raise AuditNotFoundError("audit not found")
        AUDIT_STATUS_MACHINE.transition_to(current.status, status)
        return self._audits.set_status(audit_id, status)

    def add_checklist_item(self, command: CreateChecklistItemCommand) -> ChecklistItem:
        return self._audits.add_checklist_item(command.audit_id, command.description)

    def list_checklist_items(self, audit_id: UUID) -> list[ChecklistItem]:
        return self._audits.list_checklist_items(audit_id)

    def set_checklist_item_status(
        self, item_id: UUID, status: ChecklistItemStatus, notes: str
    ) -> ChecklistItem:
        return self._audits.set_checklist_item_status(item_id, status, notes)

    def add_finding(self, command: CreateFindingCommand) -> Finding:
        return self._audits.add_finding(
            audit_id=command.audit_id,
            title=command.title,
            description=command.description,
            severity=command.severity,
            checklist_item_id=command.checklist_item_id,
        )

    def list_findings(self, audit_id: UUID) -> list[Finding]:
        return self._audits.list_findings(audit_id)

    def set_finding_status(self, finding_id: UUID, status: FindingStatus) -> Finding:
        return self._audits.set_finding_status(finding_id, status)

    def add_corrective_action(self, command: CreateCorrectiveActionCommand) -> CorrectiveAction:
        return self._audits.add_corrective_action(
            finding_id=command.finding_id,
            description=command.description,
            owner=command.owner,
            due_date=command.due_date,
        )

    def list_corrective_actions(self, finding_id: UUID) -> list[CorrectiveAction]:
        return self._audits.list_corrective_actions(finding_id)

    def set_corrective_action_status(
        self, action_id: UUID, status: CorrectiveActionStatus, now: datetime
    ) -> CorrectiveAction:
        completed_at = now if status == CorrectiveActionStatus.DONE else None
        return self._audits.set_corrective_action_status(action_id, status, completed_at)

    def build_report(self, audit_id: UUID) -> AuditReport | None:
        audit = self._audits.get_by_id(audit_id)
        if audit is None:
            return None
        checklist_items = self._audits.list_checklist_items(audit_id)
        findings = self._audits.list_findings(audit_id)
        by_severity: dict[str, int] = {}
        for finding in findings:
            by_severity[finding.severity.value] = by_severity.get(finding.severity.value, 0) + 1
        actions_total = 0
        actions_done = 0
        for finding in findings:
            actions = self._audits.list_corrective_actions(finding.id)
            actions_total += len(actions)
            actions_done += len([a for a in actions if a.status == CorrectiveActionStatus.DONE])
        return AuditReport(
            audit=audit,
            checklist_total=len(checklist_items),
            checklist_done=len([i for i in checklist_items if i.status == ChecklistItemStatus.DONE]),
            findings_by_severity=by_severity,
            open_findings=len([f for f in findings if f.status != FindingStatus.CLOSED]),
            corrective_actions_total=actions_total,
            corrective_actions_done=actions_done,
        )
