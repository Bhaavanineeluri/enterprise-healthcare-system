from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.clinical_note import ClinicalNote
from models.user import User

from repositories.clinical_note_repository import (
    create_clinical_note,
    delete_clinical_note,
    get_all_clinical_notes,
    get_clinical_note_by_id,
    get_clinical_note_count,
    update_clinical_note,
)

from repositories.emr_repository import (
    get_emr_by_id,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from repositories.doctor_repository import (
    get_doctor_by_id,
)

from schemas.clinical_note_schema import (
    ClinicalNoteCreate,
    ClinicalNoteUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_clinical_note_code(
    db: Session,
):

    count = get_clinical_note_count(
        db,
    )

    return f"CN{count + 1:06d}"


def create_clinical_note_service(
    db: Session,
    clinical_note: ClinicalNoteCreate,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        clinical_note.emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    patient = get_patient_by_id(
        db,
        clinical_note.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        clinical_note.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    new_clinical_note = ClinicalNote(

        clinical_note_code=generate_clinical_note_code(
            db,
        ),

        emr_id=clinical_note.emr_id,

        patient_id=clinical_note.patient_id,

        doctor_id=clinical_note.doctor_id,

        note_type=clinical_note.note_type,

        title=clinical_note.title,

        note=clinical_note.note,

        status="ACTIVE",
    )

    clinical_note_data = create_clinical_note(
        db,
        new_clinical_note,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="CLINICAL_NOTE",
        action="CREATE",
    )

    return clinical_note_data


def get_all_clinical_notes_service(
    db: Session,
    current_user: User,
):

    return get_all_clinical_notes(
        db,
    )


def get_clinical_note_service(
    db: Session,
    clinical_note_id: int,
    current_user: User,
):

    clinical_note = get_clinical_note_by_id(
        db,
        clinical_note_id,
    )

    if clinical_note is None:

        not_found(
            "Clinical Note not found."
        )

    return clinical_note


def update_clinical_note_service(
    db: Session,
    clinical_note_id: int,
    clinical_note_update: ClinicalNoteUpdate,
    current_user: User,
):

    clinical_note = get_clinical_note_by_id(
        db,
        clinical_note_id,
    )

    if clinical_note is None:

        not_found(
            "Clinical Note not found."
        )

    update_data = clinical_note_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            clinical_note,
            key,
            value,
        )

    updated = update_clinical_note(
        db,
        clinical_note,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="CLINICAL_NOTE",
        action="UPDATE",
    )

    return updated


def delete_clinical_note_service(
    db: Session,
    clinical_note_id: int,
    current_user: User,
):

    clinical_note = get_clinical_note_by_id(
        db,
        clinical_note_id,
    )

    if clinical_note is None:

        not_found(
            "Clinical Note not found."
        )

    delete_clinical_note(
        db,
        clinical_note,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="CLINICAL_NOTE",
        action="DELETE",
    )

    return {
        "message": "Clinical Note deleted successfully."
    }