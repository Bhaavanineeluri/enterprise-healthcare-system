from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.patient_schema import (
    PatientCreate,
    PatientUpdate,
    PatientResponse,
)

from services.patient_service import (
    create_patient_service,
    get_all_patients_service,
    get_patient_service,
    update_patient_service,
    delete_patient_service,
)


router = APIRouter(
    prefix="/patients",
    tags=["Patient Management"],
)


@router.post(
    "/",
    response_model=PatientResponse,
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_patient_service(
        db=db,
        patient=patient,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[PatientResponse],
)
def get_all_patients(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_patients_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{patient_id}",
    response_model=PatientResponse,
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_patient_service(
        db=db,
        patient_id=patient_id,
        current_user=current_user,
    )


@router.put(
    "/{patient_id}",
    response_model=PatientResponse,
)
def update_patient(
    patient_id: int,
    patient_update: PatientUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_patient_service(
        db=db,
        patient_id=patient_id,
        patient_update=patient_update,
        current_user=current_user,
    )


@router.delete(
    "/{patient_id}",
)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_patient_service(
        db=db,
        patient_id=patient_id,
        current_user=current_user,
    )