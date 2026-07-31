from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.hospital_schema import (
    HospitalCreate,
    HospitalUpdate,
    HospitalResponse,
)

from services.hospital_service import (
    create_hospital_service,
    delete_hospital_service,
    get_all_hospitals_service,
    get_hospital_service,
    update_hospital_service,
)


router = APIRouter(
    prefix="/hospitals",
    tags=["Hospital Management"],
)


@router.post(
    "/",
    response_model=HospitalResponse,
)
def create_hospital(
    hospital: HospitalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_hospital_service(
        db=db,
        hospital=hospital,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[HospitalResponse],
    
)
def get_all_hospitals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_hospitals_service(
        db=db,
        current_user=current_user,)


@router.get(
    "/{hospital_id}",
    response_model=HospitalResponse,
)
def get_hospital(
    hospital_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_hospital_service(
        db=db,
        hospital_id=hospital_id,
        current_user=current_user,
    )


@router.put(
    "/{hospital_id}",
    response_model=HospitalResponse,
)
def update_hospital(
    hospital_id: int,
    hospital_update: HospitalUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_hospital_service(
        db=db,
        hospital_id=hospital_id,
        hospital_update=hospital_update,
        current_user=current_user,
    )


@router.delete(
    "/{hospital_id}",
)
def delete_hospital(
    hospital_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_hospital_service(
        db=db,
        hospital_id=hospital_id,
        current_user=current_user,
    )