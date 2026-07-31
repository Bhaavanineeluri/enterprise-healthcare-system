from sqlalchemy.orm import Session

from models.prescription_validation import PrescriptionValidation


def create_prescription_validation(
    db: Session,
    validation: PrescriptionValidation,
):

    db.add(validation)

    db.commit()

    db.refresh(validation)

    return validation


def get_all_prescription_validations(
    db: Session,
):

    return (

        db.query(PrescriptionValidation)

        .filter(
            PrescriptionValidation.is_active == True
        )

        .all()

    )


def get_prescription_validation_by_id(
    db: Session,
    validation_id: int,
):

    return (

        db.query(PrescriptionValidation)

        .filter(
            PrescriptionValidation.id == validation_id
        )

        .first()

    )


def get_prescription_validation_count(
    db: Session,
):

    return db.query(
        PrescriptionValidation
    ).count()


def update_prescription_validation(
    db: Session,
    validation: PrescriptionValidation,
):

    db.commit()

    db.refresh(validation)

    return validation


def delete_prescription_validation(
    db: Session,
    validation: PrescriptionValidation,
):

    validation.is_active = False

    db.commit()

    db.refresh(validation)

    return validation