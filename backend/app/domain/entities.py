from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from uuid import UUID


class RiskStatus(StrEnum):
    OPEN = "open"
    MITIGATING = "mitigating"
    ACCEPTED = "accepted"
    CLOSED = "closed"


class RiskSeverity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ControlStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    RETIRED = "retired"


@dataclass(frozen=True)
class Organization:
    id: UUID
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class Risk:
    id: UUID
    organization_id: UUID
    title: str
    description: str
    severity: RiskSeverity
    status: RiskStatus
    owner: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class Control:
    id: UUID
    organization_id: UUID
    name: str
    description: str
    framework: str
    status: ControlStatus
    created_at: datetime
    updated_at: datetime
