from sqlalchemy.orm import Session

from models.clinical_note import ClinicalNote


def create_clinical_note(
    db: Session,
    clinical_note: ClinicalNote,
):

    db.add(clinical_note)

    db.commit()

    db.refresh(clinical_note)

    return clinical_note


def get_all_clinical_notes(
    db: Session,
):

    return (

        db.query(ClinicalNote)

        .filter(
            ClinicalNote.is_active == True
        )

        .all()

    )


def get_clinical_note_by_id(
    db: Session,
    clinical_note_id: int,
):

    return (

        db.query(ClinicalNote)

        .filter(
            ClinicalNote.id == clinical_note_id
        )

        .first()

    )


def get_clinical_note_count(
    db: Session,
):

    return (

        db.query(ClinicalNote)

        .count()

    )


def update_clinical_note(
    db: Session,
    clinical_note: ClinicalNote,
):

    db.commit()

    db.refresh(clinical_note)

    return clinical_note


def delete_clinical_note(
    db: Session,
    clinical_note: ClinicalNote,
):

    clinical_note.is_active = False

    db.commit()

    db.refresh(clinical_note)

    return clinical_note