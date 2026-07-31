from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.department_schema import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse,
)

from services.department_service import (
    create_department_service,
    get_all_departments_service,
    get_department_service,
    update_department_service,
    delete_department_service,
)


router = APIRouter(
    prefix="/departments",
    tags=["Department Management"],
)


@router.post(
    "/",
    response_model=DepartmentResponse,
)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_department_service(
        db=db,
        department=department,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[DepartmentResponse],
)
def get_all_departments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_departments_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_department_service(
        db=db,
        department_id=department_id,
        current_user=current_user,
    )


@router.put(
    "/{department_id}",
    response_model=DepartmentResponse,
)
def update_department(
    department_id: int,
    department_update: DepartmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_department_service(
        db=db,
        department_id=department_id,
        department_update=department_update,
        current_user=current_user,
    )


@router.delete(
    "/{department_id}",
)
def delete_department(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_department_service(
        db=db,
        department_id=department_id,
        current_user=current_user,
    )