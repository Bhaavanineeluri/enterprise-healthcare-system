from sqlalchemy.orm import Session

from models.doctor import Doctor


def create_doctor(
    db: Session,
    doctor: Doctor,
):

    db.add(doctor)

    db.commit()

    db.refresh(doctor)

    return doctor


def get_all_doctors(
    db: Session,
):

    return (

        db.query(Doctor)

        .filter(
            Doctor.is_active == True
        )

        .all()

    )


def get_doctor_by_id(
    db: Session,
    doctor_id: int,
):

    return (

        db.query(Doctor)

        .filter(
            Doctor.id == doctor_id
        )

        .first()

    )


def get_doctor_by_email(
    db: Session,
    email: str,
):

    return (

        db.query(Doctor)

        .filter(
            Doctor.email == email
        )

        .first()

    )


def get_doctor_by_license(
    db: Session,
    license_number: str,
):

    return (

        db.query(Doctor)

        .filter(
            Doctor.license_number == license_number
        )

        .first()

    )


def get_doctor_count(
    db: Session,
):

    return (

        db.query(Doctor)

        .count()

    )


def update_doctor(
    db: Session,
    doctor: Doctor,
):

    db.commit()

    db.refresh(doctor)

    return doctor


def delete_doctor(
    db: Session,
    doctor: Doctor,
):

    doctor.is_active = False

    db.commit()

    db.refresh(doctor)

    return doctor