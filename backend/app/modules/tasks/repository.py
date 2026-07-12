from datetime import date
from uuid import UUID

from backend.app.modules.tasks.models import TaskModel
from backend.app.modules.tasks.service import Task, TaskStatus
from sqlalchemy import select
from sqlalchemy.orm import Session


def to_task(model: TaskModel) -> Task:
    return Task(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        description=model.description,
        status=model.status,
        due_date=model.due_date,
        assignee=model.assignee,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


class SqlAlchemyTaskRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Task]:
        statement = (
            select(TaskModel)
            .where(TaskModel.deleted_at.is_(None))
            .where(TaskModel.organization_id == organization_id)
            .order_by(TaskModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_task(row) for row in rows]

    def get_by_id(self, task_id: UUID) -> Task | None:
        model = self._session.get(TaskModel, task_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_task(model)

    def create(
        self,
        organization_id: UUID,
        title: str,
        assignee: str,
        description: str,
        due_date: date | None,
        created_by_id: UUID | None,
    ) -> Task:
        model = TaskModel(
            organization_id=organization_id,
            title=title,
            assignee=assignee,
            description=description,
            due_date=due_date,
            status=TaskStatus.OPEN,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_task(model)

    def set_status(self, task_id: UUID, status: TaskStatus) -> Task:
        model = self._session.get(TaskModel, task_id)
        assert model is not None
        model.status = status
        self._session.commit()
        self._session.refresh(model)
        return to_task(model)
