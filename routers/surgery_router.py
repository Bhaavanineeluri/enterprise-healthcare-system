from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.surgery_schema import (
    SurgeryCreate,
    SurgeryResponse,
    SurgeryUpdate,
)

from services.surgery_service import (
    create_surgery_service,
    delete_surgery_service,
    get_all_surgeries_service,
    get_surgery_service,
    update_surgery_service,
)


router = APIRouter(
    prefix="/surgeries",
    tags=["Surgery Management"],
)


@router.post(
    "/",
    response_model=SurgeryResponse,
)
def create_surgery(
    surgery: SurgeryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_surgery_service(
        db=db,
        surgery=surgery,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[SurgeryResponse],
)
def get_all_surgeries(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_surgeries_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{surgery_id}",
    response_model=SurgeryResponse,
)
def get_surgery(
    surgery_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_surgery_service(
        db=db,
        surgery_id=surgery_id,
        current_user=current_user,
    )


@router.put(
    "/{surgery_id}",
    response_model=SurgeryResponse,
)
def update_surgery(
    surgery_id: int,
    surgery_update: SurgeryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_surgery_service(
        db=db,
        surgery_id=surgery_id,
        surgery_update=surgery_update,
        current_user=current_user,
    )


@router.delete(
    "/{surgery_id}",
)
def delete_surgery(
    surgery_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_surgery_service(
        db=db,
        surgery_id=surgery_id,
        current_user=current_user,
    )