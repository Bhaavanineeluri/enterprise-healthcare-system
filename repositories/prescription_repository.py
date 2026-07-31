from sqlalchemy.orm import Session

from models.prescription import Prescription


def create_prescription(
    db: Session,
    prescription: Prescription,
):

    db.add(prescription)

    db.commit()

    db.refresh(prescription)

    return prescription


def get_all_prescriptions(
    db: Session,
):

    return (

        db.query(Prescription)

        .filter(
            Prescription.is_active == True
        )

        .all()

    )


def get_prescription_by_id(
    db: Session,
    prescription_id: int,
):

    return (

        db.query(Prescription)

        .filter(
            Prescription.id == prescription_id
        )

        .first()

    )


def get_prescription_count(
    db: Session,
):

    return db.query(Prescription).count()


def update_prescription(
    db: Session,
    prescription: Prescription,
):

    db.commit()

    db.refresh(prescription)

    return prescription


def delete_prescription(
    db: Session,
    prescription: Prescription,
):

    prescription.is_active = False

    db.commit()

    db.refresh(prescription)

    return prescription