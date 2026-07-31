from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.staff_schema import (
    StaffCreate,
    StaffUpdate,
    StaffResponse,
)

from services.staff_service import (
    create_staff_service,
    get_all_staff_service,
    get_staff_service,
    update_staff_service,
    delete_staff_service,
)


router = APIRouter(
    prefix="/staff",
    tags=["Staff Management"],
)


@router.post(
    "/",
    response_model=StaffResponse,
)
def create_staff(
    staff: StaffCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_staff_service(
        db=db,
        staff=staff,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[StaffResponse],
)
def get_all_staff(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_staff_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{staff_id}",
    response_model=StaffResponse,
)
def get_staff(
    staff_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_staff_service(
        db=db,
        staff_id=staff_id,
        current_user=current_user,
    )


@router.put(
    "/{staff_id}",
    response_model=StaffResponse,
)
def update_staff(
    staff_id: int,
    staff_update: StaffUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_staff_service(
        db=db,
        staff_id=staff_id,
        staff_update=staff_update,
        current_user=current_user,
    )


@router.delete(
    "/{staff_id}",
)
def delete_staff(
    staff_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_staff_service(
        db=db,
        staff_id=staff_id,
        current_user=current_user,
    )