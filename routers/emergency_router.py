from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.emergency_schema import (
    EmergencyCreate,
    EmergencyUpdate,
    EmergencyResponse,
)

from services.emergency_service import (
    create_emergency_service,
    get_all_emergencies_service,
    get_emergency_service,
    update_emergency_service,
    delete_emergency_service,
)


router = APIRouter(
    prefix="/emergencies",
    tags=["Emergency Management"],
)


@router.post(
    "/",
    response_model=EmergencyResponse,
)
def create_emergency(
    emergency: EmergencyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_emergency_service(
        db=db,
        emergency=emergency,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[EmergencyResponse],
)
def get_all_emergencies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_emergencies_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{emergency_id}",
    response_model=EmergencyResponse,
)
def get_emergency(
    emergency_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_emergency_service(
        db=db,
        emergency_id=emergency_id,
        current_user=current_user,
    )


@router.put(
    "/{emergency_id}",
    response_model=EmergencyResponse,
)
def update_emergency(
    emergency_id: int,
    emergency_update: EmergencyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_emergency_service(
        db=db,
        emergency_id=emergency_id,
        emergency_update=emergency_update,
        current_user=current_user,
    )


@router.delete(
    "/{emergency_id}",
)
def delete_emergency(
    emergency_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_emergency_service(
        db=db,
        emergency_id=emergency_id,
        current_user=current_user,
    )