from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.medicine_dispensing_schema import (
    MedicineDispensingCreate,
    MedicineDispensingResponse,
    MedicineDispensingUpdate,
)

from services.medicine_dispensing_service import (
    create_medicine_dispensing_service,
    delete_medicine_dispensing_service,
    get_all_medicine_dispensings_service,
    get_medicine_dispensing_service,
    update_medicine_dispensing_service,
)


router = APIRouter(
    prefix="/medicine-dispensings",
    tags=["Medicine Dispensing"],
)


@router.post(
    "/",
    response_model=MedicineDispensingResponse,
)
def create_medicine_dispensing(
    dispensing: MedicineDispensingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_medicine_dispensing_service(
        db=db,
        dispensing=dispensing,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[MedicineDispensingResponse],
)
def get_all_medicine_dispensings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_medicine_dispensings_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{dispensing_id}",
    response_model=MedicineDispensingResponse,
)
def get_medicine_dispensing(
    dispensing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_medicine_dispensing_service(
        db=db,
        dispensing_id=dispensing_id,
        current_user=current_user,
    )


@router.put(
    "/{dispensing_id}",
    response_model=MedicineDispensingResponse,
)
def update_medicine_dispensing(
    dispensing_id: int,
    dispensing_update: MedicineDispensingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_medicine_dispensing_service(
        db=db,
        dispensing_id=dispensing_id,
        dispensing_update=dispensing_update,
        current_user=current_user,
    )


@router.delete(
    "/{dispensing_id}",
)
def delete_medicine_dispensing(
    dispensing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_medicine_dispensing_service(
        db=db,
        dispensing_id=dispensing_id,
        current_user=current_user,
    )