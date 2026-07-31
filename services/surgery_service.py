from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.surgery import Surgery
from models.user import User

from repositories.surgery_repository import (
    create_surgery,
    delete_surgery,
    get_all_surgeries,
    get_surgery_by_id,
    get_surgery_count,
    update_surgery,
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

from schemas.surgery_schema import (
    SurgeryCreate,
    SurgeryUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_surgery_code(
    db: Session,
):

    count = get_surgery_count(db)

    return f"SUR{count + 1:06d}"


def create_surgery_service(
    db: Session,
    surgery: SurgeryCreate,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        surgery.emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    patient = get_patient_by_id(
        db,
        surgery.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        surgery.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    new_surgery = Surgery(

        surgery_code=generate_surgery_code(
            db
        ),

        emr_id=surgery.emr_id,

        patient_id=surgery.patient_id,

        doctor_id=surgery.doctor_id,

        surgery_name=surgery.surgery_name,

        surgery_date=surgery.surgery_date,

        operation_theater=surgery.operation_theater,

        anesthesia_type=surgery.anesthesia_type,

        surgeon=surgery.surgeon,

        assistant_surgeon=surgery.assistant_surgeon,

        surgery_notes=surgery.surgery_notes,

        outcome=surgery.outcome,

        status="SCHEDULED",
    )

    surgery_data = create_surgery(
        db,
        new_surgery,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="SURGERY",
        action="CREATE",
    )

    return surgery_data


def get_all_surgeries_service(
    db: Session,
    current_user: User,
):

    return get_all_surgeries(
        db
    )


def get_surgery_service(
    db: Session,
    surgery_id: int,
    current_user: User,
):

    surgery = get_surgery_by_id(
        db,
        surgery_id,
    )

    if surgery is None:

        not_found(
            "Surgery not found."
        )

    return surgery


def update_surgery_service(
    db: Session,
    surgery_id: int,
    surgery_update: SurgeryUpdate,
    current_user: User,
):

    surgery = get_surgery_by_id(
        db,
        surgery_id,
    )

    if surgery is None:

        not_found(
            "Surgery not found."
        )

    update_data = surgery_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            surgery,
            key,
            value,
        )

    updated = update_surgery(
        db,
        surgery,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="SURGERY",
        action="UPDATE",
    )

    return updated


def delete_surgery_service(
    db: Session,
    surgery_id: int,
    current_user: User,
):

    surgery = get_surgery_by_id(
        db,
        surgery_id,
    )

    if surgery is None:

        not_found(
            "Surgery not found."
        )

    delete_surgery(
        db,
        surgery,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="SURGERY",
        action="DELETE",
    )

    return {
        "message": "Surgery deleted successfully."
    }