from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.opd_schema import (
    OPDCreate,
    OPDResponse,
    OPDUpdate,
)

from services.opd_service import (
    create_opd_service,
    delete_opd_service,
    get_all_opd_service,
    get_opd_service,
    update_opd_service,
)


router = APIRouter(
    prefix="/opd",
    tags=["OPD Management"],
)


@router.post(
    "/",
    response_model=OPDResponse,
)
def create_opd(
    opd: OPDCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_opd_service(
        db=db,
        opd=opd,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[OPDResponse],
)
def get_all_opd(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_opd_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{opd_id}",
    response_model=OPDResponse,
)
def get_opd(
    opd_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_opd_service(
        db=db,
        opd_id=opd_id,
        current_user=current_user,
    )


@router.put(
    "/{opd_id}",
    response_model=OPDResponse,
)
def update_opd(
    opd_id: int,
    opd_update: OPDUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_opd_service(
        db=db,
        opd_id=opd_id,
        opd_update=opd_update,
        current_user=current_user,
    )


@router.delete(
    "/{opd_id}",
)
def delete_opd(
    opd_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_opd_service(
        db=db,
        opd_id=opd_id,
        current_user=current_user,
    )