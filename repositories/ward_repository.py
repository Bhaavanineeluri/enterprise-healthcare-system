from sqlalchemy.orm import Session

from models.ward import Ward


def create_ward(
    db: Session,
    ward: Ward,
):

    db.add(ward)

    db.commit()

    db.refresh(ward)

    return ward


def get_all_wards(
    db: Session,
):

    return (

        db.query(Ward)

        .filter(
            Ward.is_active == True
        )

        .all()

    )


def get_ward_by_id(
    db: Session,
    ward_id: int,
):

    return (

        db.query(Ward)

        .filter(
            Ward.id == ward_id
        )

        .first()

    )


def get_ward_by_code(
    db: Session,
    ward_code: str,
):

    return (

        db.query(Ward)

        .filter(
            Ward.ward_code == ward_code
        )

        .first()

    )


def get_ward_count(
    db: Session,
):

    return (

        db.query(Ward)

        .count()

    )


def update_ward(
    db: Session,
    ward: Ward,
):

    db.commit()

    db.refresh(ward)

    return ward


def delete_ward(
    db: Session,
    ward: Ward,
):

    ward.is_active = False

    db.commit()

    db.refresh(ward)

    return ward