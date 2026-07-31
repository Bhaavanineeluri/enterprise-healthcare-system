from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.emr_schema import (
    EMRCreate,
    EMRResponse,
    EMRUpdate,
)

from services.emr_service import (
    create_emr_service,
    get_all_emr_service,
    get_emr_service,
    update_emr_service,
    delete_emr_service,
)


router = APIRouter(
    prefix="/emr",
    tags=["Electronic Medical Records"],
)


@router.post(
    "/",
    response_model=EMRResponse,
)
def create_emr(
    emr: EMRCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_emr_service(
        db=db,
        emr=emr,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[EMRResponse],
)
def get_all_emr(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_emr_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{emr_id}",
    response_model=EMRResponse,
)
def get_emr(
    emr_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_emr_service(
        db=db,
        emr_id=emr_id,
        current_user=current_user,
    )


@router.put(
    "/{emr_id}",
    response_model=EMRResponse,
)
def update_emr(
    emr_id: int,
    emr_update: EMRUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_emr_service(
        db=db,
        emr_id=emr_id,
        emr_update=emr_update,
        current_user=current_user,
    )


@router.delete(
    "/{emr_id}",
)
def delete_emr(
    emr_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_emr_service(
        db=db,
        emr_id=emr_id,
        current_user=current_user,
    )