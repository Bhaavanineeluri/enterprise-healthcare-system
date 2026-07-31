from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentResponse,
)

from services.appointment_service import (
    create_appointment_service,
    get_all_appointments_service,
    get_appointment_service,
    update_appointment_service,
    delete_appointment_service,
)


router = APIRouter(
    prefix="/appointments",
    tags=["Appointment Management"],
)


@router.post(
    "/",
    response_model=AppointmentResponse,
)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_appointment_service(
        db=db,
        appointment=appointment,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[AppointmentResponse],
)
def get_all_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_appointments_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{appointment_id}",
    response_model=AppointmentResponse,
)
def get_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_appointment_service(
        db=db,
        appointment_id=appointment_id,
        current_user=current_user,
    )


@router.put(
    "/{appointment_id}",
    response_model=AppointmentResponse,
)
def update_appointment(
    appointment_id: int,
    appointment_update: AppointmentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_appointment_service(
        db=db,
        appointment_id=appointment_id,
        appointment_update=appointment_update,
        current_user=current_user,
    )


@router.delete(
    "/{appointment_id}",
)
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_appointment_service(
        db=db,
        appointment_id=appointment_id,
        current_user=current_user,
    )