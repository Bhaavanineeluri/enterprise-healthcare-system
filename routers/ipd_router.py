from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.ipd_schema import (
    IPDCreate,
    IPDResponse,
    IPDUpdate,
)

from services.ipd_service import (
    create_ipd_service,
    get_all_ipd_service,
    get_ipd_service,
    update_ipd_service,
    delete_ipd_service,
)


router = APIRouter(
    prefix="/ipd",
    tags=["IPD Management"],
)


@router.post(
    "/",
    response_model=IPDResponse,
)
def create_ipd(
    ipd: IPDCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_ipd_service(
        db=db,
        ipd=ipd,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[IPDResponse],
)
def get_all_ipd(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_ipd_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{ipd_id}",
    response_model=IPDResponse,
)
def get_ipd(
    ipd_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_ipd_service(
        db=db,
        ipd_id=ipd_id,
        current_user=current_user,
    )


@router.put(
    "/{ipd_id}",
    response_model=IPDResponse,
)
def update_ipd(
    ipd_id: int,
    ipd_update: IPDUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_ipd_service(
        db=db,
        ipd_id=ipd_id,
        ipd_update=ipd_update,
        current_user=current_user,
    )


@router.delete(
    "/{ipd_id}",
)
def delete_ipd(
    ipd_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_ipd_service(
        db=db,
        ipd_id=ipd_id,
        current_user=current_user,
    )