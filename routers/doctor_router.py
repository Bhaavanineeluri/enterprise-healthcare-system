from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.doctor_schema import (
    DoctorCreate,
    DoctorUpdate,
    DoctorResponse,
)

from services.doctor_service import (
    create_doctor_service,
    get_all_doctors_service,
    get_doctor_service,
    update_doctor_service,
    delete_doctor_service,
)


router = APIRouter(
    prefix="/doctors",
    tags=["Doctor Management"],
)


@router.post(
    "/",
    response_model=DoctorResponse,
)
def create_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_doctor_service(
        db=db,
        doctor=doctor,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[DoctorResponse],
)
def get_all_doctors(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_doctors_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{doctor_id}",
    response_model=DoctorResponse,
)
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_doctor_service(
        db=db,
        doctor_id=doctor_id,
        current_user=current_user,
    )


@router.put(
    "/{doctor_id}",
    response_model=DoctorResponse,
)
def update_doctor(
    doctor_id: int,
    doctor_update: DoctorUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_doctor_service(
        db=db,
        doctor_id=doctor_id,
        doctor_update=doctor_update,
        current_user=current_user,
    )


@router.delete(
    "/{doctor_id}",
)
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_doctor_service(
        db=db,
        doctor_id=doctor_id,
        current_user=current_user,
    )