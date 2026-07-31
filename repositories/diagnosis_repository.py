from sqlalchemy.orm import Session

from models.diagnosis import Diagnosis


def create_diagnosis(
    db: Session,
    diagnosis: Diagnosis,
):

    db.add(diagnosis)

    db.commit()

    db.refresh(diagnosis)

    return diagnosis


def get_all_diagnosis(
    db: Session,
):

    return (

        db.query(Diagnosis)

        .filter(
            Diagnosis.is_active == True
        )

        .all()

    )


def get_diagnosis_by_id(
    db: Session,
    diagnosis_id: int,
):

    return (

        db.query(Diagnosis)

        .filter(
            Diagnosis.id == diagnosis_id
        )

        .first()

    )


def get_diagnosis_count(
    db: Session,
):

    return (

        db.query(Diagnosis)

        .count()

    )


def update_diagnosis(
    db: Session,
    diagnosis: Diagnosis,
):

    db.commit()

    db.refresh(diagnosis)

    return diagnosis


def delete_diagnosis(
    db: Session,
    diagnosis: Diagnosis,
):

    diagnosis.is_active = False

    db.commit()

    db.refresh(diagnosis)

    return diagnosis
