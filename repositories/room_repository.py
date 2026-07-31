from sqlalchemy.orm import Session

from models.room import Room


def create_room(
    db: Session,
    room: Room,
):

    db.add(room)

    db.commit()

    db.refresh(room)

    return room


def get_all_rooms(
    db: Session,
):

    return (

        db.query(Room)

        .filter(
            Room.is_active == True
        )

        .all()

    )


def get_room_by_id(
    db: Session,
    room_id: int,
):

    return (

        db.query(Room)

        .filter(
            Room.id == room_id
        )

        .first()

    )


def get_room_by_number(
    db: Session,
    room_number: str,
):

    return (

        db.query(Room)

        .filter(
            Room.room_number == room_number
        )

        .first()

    )


def get_room_count(
    db: Session,
):

    return db.query(Room).count()


def update_room(
    db: Session,
    room: Room,
):

    db.commit()

    db.refresh(room)

    return room


def delete_room(
    db: Session,
    room: Room,
):

    room.is_active = False

    db.commit()

    db.refresh(room)

    return room