from dataclasses import dataclass
from datetime import date, datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID

from backend.app.workflow.state_machine import StateMachine, Transition


class TaskStatus(StrEnum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    DONE = "done"


TASK_STATUS_MACHINE: StateMachine[TaskStatus] = StateMachine(
    [
        Transition("start", TaskStatus.OPEN, TaskStatus.IN_PROGRESS),
        Transition("complete", TaskStatus.IN_PROGRESS, TaskStatus.DONE),
        Transition("reopen", TaskStatus.DONE, TaskStatus.IN_PROGRESS),
    ]
)


@dataclass(frozen=True)
class Task:
    id: UUID
    organization_id: UUID
    title: str
    description: str
    status: TaskStatus
    due_date: date | None
    assignee: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateTaskCommand:
    organization_id: UUID
    title: str
    assignee: str
    description: str = ""
    due_date: date | None = None
    created_by_id: UUID | None = None


class TaskNotFoundError(Exception):
    pass


class TaskStore(Protocol):
    def list(self, organization_id: UUID) -> list[Task]:
        raise NotImplementedError

    def get_by_id(self, task_id: UUID) -> Task | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        title: str,
        assignee: str,
        description: str,
        due_date: date | None,
        created_by_id: UUID | None,
    ) -> Task:
        raise NotImplementedError

    def set_status(self, task_id: UUID, status: TaskStatus) -> Task:
        raise NotImplementedError


class TaskService:
    def __init__(self, tasks: TaskStore) -> None:
        self._tasks = tasks

    def list_tasks(self, organization_id: UUID) -> list[Task]:
        return self._tasks.list(organization_id)

    def get_task(self, task_id: UUID) -> Task | None:
        return self._tasks.get_by_id(task_id)

    def create_task(self, command: CreateTaskCommand) -> Task:
        return self._tasks.create(
            organization_id=command.organization_id,
            title=command.title,
            assignee=command.assignee,
            description=command.description,
            due_date=command.due_date,
            created_by_id=command.created_by_id,
        )

    def set_status(self, task_id: UUID, status: TaskStatus) -> Task:
        current = self._tasks.get_by_id(task_id)
        if current is None:
            raise TaskNotFoundError("task not found")
        TASK_STATUS_MACHINE.transition_to(current.status, status)
        return self._tasks.set_status(task_id, status)
