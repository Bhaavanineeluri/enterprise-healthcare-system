from sqlalchemy.orm import Session

from models.hospital import Hospital


def create_hospital(
    db: Session,
    hospital: Hospital,
):

    db.add(hospital)

    db.commit()

    db.refresh(hospital)

    return hospital


def get_all_hospitals(
    db: Session,
):

    return (

        db.query(Hospital)

        .filter(
            Hospital.is_active == True
        )

        .all()

    )


def get_hospital_by_id(
    db: Session,
    hospital_id: int,
):

    return (

        db.query(Hospital)

        .filter(
            Hospital.id == hospital_id
        )

        .first()

    )


def get_hospital_by_code(
    db: Session,
    hospital_code: str,
):

    return (

        db.query(Hospital)

        .filter(
            Hospital.hospital_code == hospital_code
        )

        .first()

    )


def get_hospital_by_email(
    db: Session,
    email: str,
):

    return (

        db.query(Hospital)

        .filter(
            Hospital.email == email
        )

        .first()

    )


def get_hospital_by_registration_number(
    db: Session,
    registration_number: str,
):

    return (

        db.query(Hospital)

        .filter(
            Hospital.registration_number == registration_number
        )

        .first()

    )


def get_hospital_by_license_number(
    db: Session,
    license_number: str,
):

    return (

        db.query(Hospital)

        .filter(
            Hospital.license_number == license_number
        )

        .first()

    )


def update_hospital(
    db: Session,
    hospital: Hospital,
):

    db.commit()

    db.refresh(hospital)

    return hospital


def delete_hospital(
    db: Session,
    hospital: Hospital,
):

    hospital.is_active = False

    db.commit()

    db.refresh(hospital)

    return hospital


def get_hospital_count(
    db: Session,
):

    return (

        db.query(Hospital)

        .count()

    )