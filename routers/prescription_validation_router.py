from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.dependencies import  get_db
from dependencies.auth import get_current_user
from models.user import User

from schemas.prescription_validation_schema import (
    PrescriptionValidationCreate,
    PrescriptionValidationResponse,
    PrescriptionValidationUpdate,
)

from services.prescription_validation_service import (
    create_prescription_validation_service,
    get_all_prescription_validations_service,
    get_prescription_validation_service,
    update_prescription_validation_service,
    delete_prescription_validation_service,
)

router = APIRouter(
    prefix="/prescription-validations",
    tags=["Prescription Validation"],
)


@router.post(
    "/",
    response_model=PrescriptionValidationResponse,
)
def create_prescription_validation(
    validation: PrescriptionValidationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_prescription_validation_service(
        db=db,
        validation=validation,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[PrescriptionValidationResponse],
)
def get_all_prescription_validations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_prescription_validations_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{validation_id}",
    response_model=PrescriptionValidationResponse,
)
def get_prescription_validation(
    validation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_prescription_validation_service(
        db=db,
        validation_id=validation_id,
        current_user=current_user,
    )


@router.put(
    "/{validation_id}",
    response_model=PrescriptionValidationResponse,
)
def update_prescription_validation(
    validation_id: int,
    validation_update: PrescriptionValidationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_prescription_validation_service(
        db=db,
        validation_id=validation_id,
        validation_update=validation_update,
        current_user=current_user,
    )


@router.delete(
    "/{validation_id}",
)
def delete_prescription_validation(
    validation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_prescription_validation_service(
        db=db,
        validation_id=validation_id,
        current_user=current_user,
    )