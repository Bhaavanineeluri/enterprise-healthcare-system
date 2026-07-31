from sqlalchemy.orm import Session

from models.emergency import Emergency


def create_emergency(
    db: Session,
    emergency: Emergency,
):

    db.add(emergency)

    db.commit()

    db.refresh(emergency)

    return emergency


def get_all_emergencies(
    db: Session,
):

    return (

        db.query(Emergency)

        .filter(
            Emergency.is_active == True
        )

        .all()

    )


def get_emergency_by_id(
    db: Session,
    emergency_id: int,
):

    return (

        db.query(Emergency)

        .filter(
            Emergency.id == emergency_id
        )

        .first()

    )


def get_emergency_by_code(
    db: Session,
    emergency_code: str,
):

    return (

        db.query(Emergency)

        .filter(
            Emergency.emergency_code == emergency_code
        )

        .first()

    )


def get_emergency_count(
    db: Session,
):

    return (

        db.query(Emergency)

        .count()

    )


def update_emergency(
    db: Session,
    emergency: Emergency,
):

    db.commit()

    db.refresh(emergency)

    return emergency


def delete_emergency(
    db: Session,
    emergency: Emergency,
):

    emergency.is_active = False

    db.commit()

    db.refresh(emergency)

    return emergency