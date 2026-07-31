from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (get_db)
from dependencies.auth import get_current_user
from models.user import User

from schemas.diagnosis_schema import (
    DiagnosisCreate,
    DiagnosisResponse,
    DiagnosisUpdate,
)

from services.diagnosis_service import (
    create_diagnosis_service,
    get_all_diagnosis_service,
    get_diagnosis_service,
    update_diagnosis_service,
    delete_diagnosis_service,
)


router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis Management"],
)


@router.post(
    "/",
    response_model=DiagnosisResponse,
)
def create_diagnosis(
    diagnosis: DiagnosisCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_diagnosis_service(
        db=db,
        diagnosis=diagnosis,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[DiagnosisResponse],
)
def get_all_diagnosis(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_diagnosis_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{diagnosis_id}",
    response_model=DiagnosisResponse,
)
def get_diagnosis(
    diagnosis_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_diagnosis_service(
        db=db,
        diagnosis_id=diagnosis_id,
        current_user=current_user,
    )


@router.put(
    "/{diagnosis_id}",
    response_model=DiagnosisResponse,
)
def update_diagnosis(
    diagnosis_id: int,
    diagnosis_update: DiagnosisUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_diagnosis_service(
        db=db,
        diagnosis_id=diagnosis_id,
        diagnosis_update=diagnosis_update,
        current_user=current_user,
    )


@router.delete(
    "/{diagnosis_id}",
)
def delete_diagnosis(
    diagnosis_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_diagnosis_service(
        db=db,
        diagnosis_id=diagnosis_id,
        current_user=current_user,
    )