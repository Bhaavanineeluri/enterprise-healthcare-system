from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.ambulance_schema import (
    AmbulanceCreate,
    AmbulanceUpdate,
    AmbulanceResponse,
)

from services.ambulance_service import (
    create_ambulance_service,
    get_all_ambulances_service,
    get_ambulance_service,
    update_ambulance_service,
    delete_ambulance_service,
)


router = APIRouter(
    prefix="/ambulances",
    tags=["Ambulance Management"],
)


@router.post(
    "/",
    response_model=AmbulanceResponse,
)
def create_ambulance(
    ambulance: AmbulanceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_ambulance_service(
        db=db,
        ambulance=ambulance,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[AmbulanceResponse],
)
def get_all_ambulances(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_ambulances_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{ambulance_id}",
    response_model=AmbulanceResponse,
    
)
def get_ambulance(
    ambulance_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_ambulance_service(
        db=db,
        ambulance_id=ambulance_id,
        current_user=current_user,
    )


@router.put(
    "/{ambulance_id}",
    response_model=AmbulanceResponse,
)
def update_ambulance(
    ambulance_id: int,
    ambulance_update: AmbulanceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_ambulance_service(
        db=db,
        ambulance_id=ambulance_id,
        ambulance_update=ambulance_update,
        current_user=current_user,
    )


@router.delete(
    "/{ambulance_id}",
)
def delete_ambulance(
    ambulance_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_ambulance_service(
        db=db,
        ambulance_id=ambulance_id,
        current_user=current_user,
    )