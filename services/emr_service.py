from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.emr import EMR
from models.user import User

from repositories.emr_repository import (
    create_emr,
    delete_emr,
    get_all_emr,
    get_emr_by_id,
    get_emr_count,
    update_emr,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from repositories.doctor_repository import (
    get_doctor_by_id,
)

from repositories.opd_repository import (
    get_opd_by_id,
)

from repositories.ipd_repository import (
    get_ipd_by_id,
)

from schemas.emr_schema import (
    EMRCreate,
    EMRUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_emr_code(
    db: Session,
):

    count = get_emr_count(db)

    return f"EMR{count + 1:06d}"


def create_emr_service(
    db: Session,
    emr: EMRCreate,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        emr.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        emr.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    if emr.opd_id is None and emr.ipd_id is None:

        bad_request(
            "Either OPD or IPD must be provided."
        )

    if emr.opd_id is not None:

        opd = get_opd_by_id(
            db,
            emr.opd_id,
        )

        if opd is None:

            not_found(
                "OPD record not found."
            )

    if emr.ipd_id is not None:

        ipd = get_ipd_by_id(
            db,
            emr.ipd_id,
        )

        if ipd is None:

            not_found(
                "IPD record not found."
            )

    new_emr = EMR(

        emr_code=generate_emr_code(
            db
        ),

        patient_id=emr.patient_id,

        doctor_id=emr.doctor_id,

        opd_id=emr.opd_id,

        ipd_id=emr.ipd_id,

        chief_complaint=emr.chief_complaint,

        medical_history=emr.medical_history,

        family_history=emr.family_history,

        allergy_history=emr.allergy_history,

        examination=emr.examination,

        diagnosis_summary=emr.diagnosis_summary,

        treatment_summary=emr.treatment_summary,

        status="ACTIVE",
    )

    emr_data = create_emr(
        db,
        new_emr,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EMR",
        action="CREATE",
    )

    return emr_data


def get_all_emr_service(
    db: Session,
    current_user: User,
):

    return get_all_emr(
        db
    )


def get_emr_service(
    db: Session,
    emr_id: int,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    return emr


def update_emr_service(
    db: Session,
    emr_id: int,
    emr_update: EMRUpdate,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    update_data = emr_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            emr,
            key,
            value,
        )

    updated = update_emr(
        db,
        emr,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EMR",
        action="UPDATE",
    )

    return updated


def delete_emr_service(
    db: Session,
    emr_id: int,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    delete_emr(
        db,
        emr,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EMR",
        action="DELETE",
    )

    return {
        "message": "EMR deleted successfully."
    }