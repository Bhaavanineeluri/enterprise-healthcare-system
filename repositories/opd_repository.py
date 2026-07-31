from sqlalchemy.orm import Session

from models.opd import OPD


def create_opd(
    db: Session,
    opd: OPD,
):

    db.add(opd)

    db.commit()

    db.refresh(opd)

    return opd


def get_all_opd(
    db: Session,
):

    return (

        db.query(OPD)

        .filter(
            OPD.is_active == True
        )

        .all()

    )


def get_opd_by_id(
    db: Session,
    opd_id: int,
):

    return (

        db.query(OPD)

        .filter(
            OPD.id == opd_id
        )

        .first()

    )


def get_opd_by_appointment(
    db: Session,
    appointment_id: int,
):

    return (

        db.query(OPD)

        .filter(
            OPD.appointment_id == appointment_id
        )

        .first()

    )


def get_opd_count(
    db: Session,
):

    return (

        db.query(OPD)

        .count()

    )


def get_next_token_number(
    db: Session,
):

    token = (

        db.query(OPD)

        .count()

    )

    return token + 1


def update_opd(
    db: Session,
    opd: OPD,
):

    db.commit()

    db.refresh(opd)

    return opd


def delete_opd(
    db: Session,
    opd: OPD,
):

    opd.is_active = False

    db.commit()

    db.refresh(opd)

    return opd