from sqlalchemy.orm import Session

from models.staff import Staff


def create_staff(
    db: Session,
    staff: Staff,
):

    db.add(staff)

    db.commit()

    db.refresh(staff)

    return staff


def get_all_staff(
    db: Session,
):

    return (

        db.query(Staff)

        .filter(
            Staff.is_active == True
        )

        .all()

    )


def get_staff_by_id(
    db: Session,
    staff_id: int,
):

    return (

        db.query(Staff)

        .filter(
            Staff.id == staff_id
        )

        .first()

    )


def get_staff_by_email(
    db: Session,
    email: str,
):

    return (

        db.query(Staff)

        .filter(
            Staff.email == email
        )

        .first()

    )


def get_staff_count(
    db: Session,
):

    return (

        db.query(Staff)

        .count()

    )


def update_staff(
    db: Session,
    staff: Staff,
):

    db.commit()

    db.refresh(staff)

    return staff


def delete_staff(
    db: Session,
    staff: Staff,
):

    staff.is_active = False

    db.commit()

    db.refresh(staff)

    return staff