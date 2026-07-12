from uuid import UUID

from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_task_service,
    require_permission,
)
from backend.app.modules.tasks.schemas import TaskCreate, TaskRead, TaskStatusUpdate
from backend.app.modules.tasks.service import CreateTaskCommand, Task, TaskService
from backend.app.modules.users.service import User
from backend.app.security.permissions import TASKS_MANAGE, TASKS_READ
from backend.app.workflow.state_machine import IllegalTransitionError
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


def _owned_task(task_id: UUID, current_user: User, service: TaskService) -> Task:
    task = service.get_task(task_id)
    if task is None or task.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    return task


@router.get(
    "",
    response_model=list[TaskRead],
    dependencies=[Depends(require_permission(TASKS_READ))],
)
def list_tasks(
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
) -> list[TaskRead]:
    return [TaskRead.model_validate(item) for item in service.list_tasks(current_user.organization_id)]


@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(TASKS_MANAGE))],
)
def create_task(
    payload: TaskCreate,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    task = service.create_task(
        CreateTaskCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return TaskRead.model_validate(task)


@router.get(
    "/{task_id}",
    response_model=TaskRead,
    dependencies=[Depends(require_permission(TASKS_READ))],
)
def get_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    task = _owned_task(task_id, current_user, service)
    return TaskRead.model_validate(task)


@router.patch(
    "/{task_id}/status",
    response_model=TaskRead,
    dependencies=[Depends(require_permission(TASKS_MANAGE))],
)
def update_task_status(
    task_id: UUID,
    payload: TaskStatusUpdate,
    current_user: User = Depends(get_current_user),
    service: TaskService = Depends(get_task_service),
) -> TaskRead:
    _owned_task(task_id, current_user, service)
    try:
        task = service.set_status(task_id, payload.status)
    except IllegalTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return TaskRead.model_validate(task)
