from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.prescription_schema import (
    PrescriptionCreate,
    PrescriptionResponse,
    PrescriptionUpdate,
)

from services.prescription_service import (
    create_prescription_service,
    get_all_prescriptions_service,
    get_prescription_service,
    update_prescription_service,
    delete_prescription_service,
)


router = APIRouter(
    prefix="/prescriptions",
    tags=["Prescription Management"],
)


@router.post(
    "/",
    response_model=PrescriptionResponse,
)
def create_prescription(
    prescription: PrescriptionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_prescription_service(
        db=db,
        prescription=prescription,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[PrescriptionResponse],
)
def get_all_prescriptions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_prescriptions_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{prescription_id}",
    response_model=PrescriptionResponse,
)
def get_prescription(
    prescription_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_prescription_service(
        db=db,
        prescription_id=prescription_id,
        current_user=current_user,
    )


@router.put(
    "/{prescription_id}",
    response_model=PrescriptionResponse,
)
def update_prescription(
    prescription_id: int,
    prescription_update: PrescriptionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_prescription_service(
        db=db,
        prescription_id=prescription_id,
        prescription_update=prescription_update,
        current_user=current_user,
    )


@router.delete(
    "/{prescription_id}",
)
def delete_prescription(
    prescription_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_prescription_service(
        db=db,
        prescription_id=prescription_id,
        current_user=current_user,
    )