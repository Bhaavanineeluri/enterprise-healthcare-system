from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.room import Room
from models.user import User

from repositories.room_repository import (
    create_room,
    delete_room,
    get_all_rooms,
    get_room_by_id,
    get_room_by_number,
    get_room_count,
    update_room,
)

from repositories.ward_repository import (
    get_ward_by_id,
)

from schemas.room_schema import (
    RoomCreate,
    RoomUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_room_code(
    db: Session,
):

    count = get_room_count(db)

    return f"ROM{count + 1:06d}"


def create_room_service(
    db: Session,
    room: RoomCreate,
    current_user: User,
):

    ward = get_ward_by_id(
        db,
        room.ward_id,
    )

    if ward is None:

        not_found(
            "Ward not found."
        )

    existing = get_room_by_number(
        db,
        room.room_number,
    )

    if existing:

        bad_request(
            "Room number already exists."
        )

    new_room = Room(

        room_code=generate_room_code(
            db
        ),

        ward_id=room.ward_id,

        room_number=room.room_number,

        room_type=room.room_type,

        floor=room.floor,

        total_beds=room.total_beds,

        occupied_beds=0,

        room_status="AVAILABLE",
    )

    room_data = create_room(
        db,
        new_room,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="ROOM",
        action="CREATE",
    )

    return room_data


def get_all_rooms_service(
    db: Session,
    current_user: User,
):

    return get_all_rooms(
        db
    )


def get_room_service(
    db: Session,
    room_id: int,
    current_user: User,
):

    room = get_room_by_id(
        db,
        room_id,
    )

    if room is None:

        not_found(
            "Room not found."
        )

    return room


def update_room_service(
    db: Session,
    room_id: int,
    room_update: RoomUpdate,
    current_user: User,
):

    room = get_room_by_id(
        db,
        room_id,
    )

    if room is None:

        not_found(
            "Room not found."
        )

    update_data = room_update.model_dump(
        exclude_unset=True
    )

    if (
        "ward_id" in update_data
    ):

        ward = get_ward_by_id(
            db,
            update_data["ward_id"],
        )

        if ward is None:

            not_found(
                "Ward not found."
            )

    if (
        "room_number" in update_data
        and
        update_data["room_number"] != room.room_number
    ):

        existing = get_room_by_number(
            db,
            update_data["room_number"],
        )

        if existing:

            bad_request(
                "Room number already exists."
            )

    for key, value in update_data.items():

        setattr(
            room,
            key,
            value,
        )

    updated = update_room(
        db,
        room,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="ROOM",
        action="UPDATE",
    )

    return updated


def delete_room_service(
    db: Session,
    room_id: int,
    current_user: User,
):

    room = get_room_by_id(
        db,
        room_id,
    )

    if room is None:

        not_found(
            "Room not found."
        )

    delete_room(
        db,
        room,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="ROOM",
        action="DELETE",
    )

    return {
        "message": "Room deleted successfully."
    }