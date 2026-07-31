from sqlalchemy.orm import Session

from models.emr import EMR


def create_emr(
    db: Session,
    emr: EMR,
):

    db.add(emr)

    db.commit()

    db.refresh(emr)

    return emr


def get_all_emr(
    db: Session,
):

    return (

        db.query(EMR)

        .filter(
            EMR.is_active == True
        )

        .all()

    )


def get_emr_by_id(
    db: Session,
    emr_id: int,
):

    return (

        db.query(EMR)

        .filter(
            EMR.id == emr_id
        )

        .first()

    )


def get_emr_count(
    db: Session,
):

    return (

        db.query(EMR)

        .count()

    )


def update_emr(
    db: Session,
    emr: EMR,
):

    db.commit()

    db.refresh(emr)

    return emr


def delete_emr(
    db: Session,
    emr: EMR,
):

    emr.is_active = False

    db.commit()

    db.refresh(emr)

    return emr