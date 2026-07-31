from sqlalchemy.orm import Session

from models.ambulance import Ambulance


def create_ambulance(
    db: Session,
    ambulance: Ambulance,
):

    db.add(ambulance)

    db.commit()

    db.refresh(ambulance)

    return ambulance


def get_all_ambulances(
    db: Session,
):

    return (

        db.query(Ambulance)

        .filter(
            Ambulance.is_active == True
        )

        .all()

    )


def get_ambulance_by_id(
    db: Session,
    ambulance_id: int,
):

    return (

        db.query(Ambulance)

        .filter(
            Ambulance.id == ambulance_id
        )

        .first()

    )


def get_ambulance_by_vehicle_number(
    db: Session,
    vehicle_number: str,
):

    return (

        db.query(Ambulance)

        .filter(
            Ambulance.vehicle_number == vehicle_number
        )

        .first()

    )


def get_ambulance_count(
    db: Session,
):

    return (

        db.query(Ambulance)

        .count()

    )


def update_ambulance(
    db: Session,
    ambulance: Ambulance,
):

    db.commit()

    db.refresh(ambulance)

    return ambulance


def delete_ambulance(
    db: Session,
    ambulance: Ambulance,
):

    ambulance.is_active = False

    db.commit()

    db.refresh(ambulance)

    return ambulance