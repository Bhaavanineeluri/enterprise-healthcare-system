from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.bed_schema import (
    BedCreate,
    BedUpdate,
    BedResponse,
)

from services.bed_service import (
    create_bed_service,
    get_all_beds_service,
    get_bed_service,
    update_bed_service,
    delete_bed_service,
)


router = APIRouter(
    prefix="/beds",
    tags=["Bed Management"],
)


@router.post(
    "/",
    response_model=BedResponse,
)
def create_bed(
    bed: BedCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_bed_service(
        db=db,
        bed=bed,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[BedResponse],
)
def get_all_beds(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_beds_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{bed_id}",
    response_model=BedResponse,
)
def get_bed(
    bed_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_bed_service(
        db=db,
        bed_id=bed_id,
        current_user=current_user,
    )


@router.put(
    "/{bed_id}",
    response_model=BedResponse,
)
def update_bed(
    bed_id: int,
    bed_update: BedUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_bed_service(
        db=db,
        bed_id=bed_id,
        bed_update=bed_update,
        current_user=current_user,
    )


@router.delete(
    "/{bed_id}",
)
def delete_bed(
    bed_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_bed_service(
        db=db,
        bed_id=bed_id,
        current_user=current_user,
    )