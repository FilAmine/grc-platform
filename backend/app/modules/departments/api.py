from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_department_service,
    require_permission,
)
from backend.app.modules.departments.schemas import DepartmentCreate, DepartmentRead
from backend.app.modules.departments.service import CreateDepartmentCommand, DepartmentService
from backend.app.modules.users.service import User
from backend.app.security.permissions import DEPARTMENTS_MANAGE, DEPARTMENTS_READ
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "",
    response_model=list[DepartmentRead],
    dependencies=[Depends(require_permission(DEPARTMENTS_READ))],
)
def list_departments(
    current_user: User = Depends(get_current_user),
    service: DepartmentService = Depends(get_department_service),
) -> list[DepartmentRead]:
    return [
        DepartmentRead.model_validate(item)
        for item in service.list_departments(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=DepartmentRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(DEPARTMENTS_MANAGE))],
)
def create_department(
    payload: DepartmentCreate,
    current_user: User = Depends(get_current_user),
    service: DepartmentService = Depends(get_department_service),
) -> DepartmentRead:
    if payload.parent_department_id is not None:
        parent = service.get_department(payload.parent_department_id)
        if parent is None or parent.organization_id != current_user.organization_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="parent department not found")

    department = service.create_department(
        CreateDepartmentCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return DepartmentRead.model_validate(department)
