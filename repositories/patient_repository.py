from sqlalchemy.orm import Session

from models.patient import Patient


def create_patient(
    db: Session,
    patient: Patient,
):

    db.add(patient)

    db.commit()

    db.refresh(patient)

    return patient


def get_all_patients(
    db: Session,
):

    return (

        db.query(Patient)

        .filter(
            Patient.is_active == True
        )

        .all()

    )


def get_patient_by_id(
    db: Session,
    patient_id: int,
):

    return (

        db.query(Patient)

        .filter(
            Patient.id == patient_id
        )

        .first()

    )


def get_patient_by_email(
    db: Session,
    email: str,
):

    return (

        db.query(Patient)

        .filter(
            Patient.email == email
        )

        .first()

    )


def get_patient_by_phone(
    db: Session,
    phone: str,
):

    return (

        db.query(Patient)

        .filter(
            Patient.phone == phone
        )

        .first()

    )


def get_patient_by_aadhaar(
    db: Session,
    aadhaar_number: str,
):

    return (

        db.query(Patient)

        .filter(
            Patient.aadhaar_number == aadhaar_number
        )

        .first()

    )


def get_patient_count(
    db: Session,
):

    return (

        db.query(Patient)

        .count()

    )


def update_patient(
    db: Session,
    patient: Patient,
):

    db.commit()

    db.refresh(patient)

    return patient


def delete_patient(
    db: Session,
    patient: Patient,
):

    patient.is_active = False

    db.commit()

    db.refresh(patient)

    return patient