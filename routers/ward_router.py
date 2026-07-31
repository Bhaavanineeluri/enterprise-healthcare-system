from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.ward_schema import (
    WardCreate,
    WardUpdate,
    WardResponse,
)

from services.ward_service import (
    create_ward_service,
    get_all_wards_service,
    get_ward_service,
    update_ward_service,
    delete_ward_service,
)


router = APIRouter(
    prefix="/wards",
    tags=["Ward Management"],
)


@router.post(
    "/",
    response_model=WardResponse,
)
def create_ward(
    ward: WardCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_ward_service(
        db=db,
        ward=ward,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[WardResponse],
)
def get_all_wards(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_wards_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{ward_id}",
    response_model=WardResponse,
)
def get_ward(
    ward_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_ward_service(
        db=db,
        ward_id=ward_id,
        current_user=current_user,
    )


@router.put(
    "/{ward_id}",
    response_model=WardResponse,
)
def update_ward(
    ward_id: int,
    ward_update: WardUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_ward_service(
        db=db,
        ward_id=ward_id,
        ward_update=ward_update,
        current_user=current_user,
    )


@router.delete(
    "/{ward_id}",
)
def delete_ward(
    ward_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_ward_service(
        db=db,
        ward_id=ward_id,
        current_user=current_user,
    )