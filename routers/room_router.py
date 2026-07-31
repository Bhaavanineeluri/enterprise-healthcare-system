from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.room_schema import (
    RoomCreate,
    RoomUpdate,
    RoomResponse,
)

from services.room_service import (
    create_room_service,
    get_all_rooms_service,
    get_room_service,
    update_room_service,
    delete_room_service,
)


router = APIRouter(
    prefix="/rooms",
    tags=["Room Management"],
)


@router.post(
    "/",
    response_model=RoomResponse,
)
def create_room(
    room: RoomCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_room_service(
        db=db,
        room=room,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[RoomResponse],
)
def get_all_rooms(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_rooms_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{room_id}",
    response_model=RoomResponse,
)
def get_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_room_service(
        db=db,
        room_id=room_id,
        current_user=current_user,
    )


@router.put(
    "/{room_id}",
    response_model=RoomResponse,
)
def update_room(
    room_id: int,
    room_update: RoomUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_room_service(
        db=db,
        room_id=room_id,
        room_update=room_update,
        current_user=current_user,
    )


@router.delete(
    "/{room_id}",
)
def delete_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_room_service(
        db=db,
        room_id=room_id,
        current_user=current_user,
    )