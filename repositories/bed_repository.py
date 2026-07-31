from sqlalchemy.orm import Session

from models.bed import Bed


def create_bed(
    db: Session,
    bed: Bed,
):

    db.add(bed)

    db.commit()

    db.refresh(bed)

    return bed


def get_all_beds(
    db: Session,
):

    return (

        db.query(Bed)

        .filter(
            Bed.is_active == True
        )

        .all()

    )


def get_bed_by_id(
    db: Session,
    bed_id: int,
):

    return (

        db.query(Bed)

        .filter(
            Bed.id == bed_id
        )

        .first()

    )


def get_bed_by_number(
    db: Session,
    bed_number: str,
):

    return (

        db.query(Bed)

        .filter(
            Bed.bed_number == bed_number
        )

        .first()

    )


def get_bed_count(
    db: Session,
):

    return (

        db.query(Bed)

        .count()

    )


def update_bed(
    db: Session,
    bed: Bed,
):

    db.commit()

    db.refresh(bed)

    return bed


def delete_bed(
    db: Session,
    bed: Bed,
):

    bed.is_active = False

    db.commit()

    db.refresh(bed)

    return bed