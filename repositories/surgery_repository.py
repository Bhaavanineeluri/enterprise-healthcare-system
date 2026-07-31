from sqlalchemy.orm import Session

from models.surgery import Surgery


def create_surgery(
    db: Session,
    surgery: Surgery,
):

    db.add(surgery)

    db.commit()

    db.refresh(surgery)

    return surgery


def get_all_surgeries(
    db: Session,
):

    return (

        db.query(Surgery)

        .filter(
            Surgery.is_active == True
        )

        .all()

    )


def get_surgery_by_id(
    db: Session,
    surgery_id: int,
):

    return (

        db.query(Surgery)

        .filter(
            Surgery.id == surgery_id
        )

        .first()

    )


def get_surgery_count(
    db: Session,
):

    return db.query(Surgery).count()


def update_surgery(
    db: Session,
    surgery: Surgery,
):

    db.commit()

    db.refresh(surgery)

    return surgery


def delete_surgery(
    db: Session,
    surgery: Surgery,
):

    surgery.is_active = False

    db.commit()

    db.refresh(surgery)

    return surgery