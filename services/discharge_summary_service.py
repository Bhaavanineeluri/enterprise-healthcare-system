from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.discharge_summary import DischargeSummary
from models.user import User

from repositories.discharge_summary_repository import (
    create_discharge_summary,
    delete_discharge_summary,
    get_all_discharge_summaries,
    get_discharge_summary_by_id,
    get_discharge_summary_count,
    update_discharge_summary,
)

from repositories.ipd_repository import (
    get_ipd_by_id,
    update_ipd,
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

from repositories.bed_repository import (
    get_bed_by_id,
    update_bed,
)

from schemas.discharge_summary_schema import (
    DischargeSummaryCreate,
    DischargeSummaryUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_discharge_summary_code(
    db: Session,
):

    count = get_discharge_summary_count(db)

    return f"DS{count + 1:06d}"


def create_discharge_summary_service(
    db: Session,
    discharge_summary: DischargeSummaryCreate,
    current_user: User,
):

    ipd = get_ipd_by_id(
        db,
        discharge_summary.ipd_id,
    )

    if ipd is None:

        not_found(
            "IPD record not found."
        )

    emr = get_emr_by_id(
        db,
        discharge_summary.emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    patient = get_patient_by_id(
        db,
        discharge_summary.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        discharge_summary.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    new_summary = DischargeSummary(

        discharge_summary_code=generate_discharge_summary_code(
            db
        ),

        ipd_id=discharge_summary.ipd_id,

        emr_id=discharge_summary.emr_id,

        patient_id=discharge_summary.patient_id,

        doctor_id=discharge_summary.doctor_id,

        admission_date=discharge_summary.admission_date,

        discharge_date=discharge_summary.discharge_date,

        final_diagnosis=discharge_summary.final_diagnosis,

        procedures_performed=discharge_summary.procedures_performed,

        hospital_course=discharge_summary.hospital_course,

        condition_at_discharge=discharge_summary.condition_at_discharge,

        discharge_medications=discharge_summary.discharge_medications,

        follow_up_instructions=discharge_summary.follow_up_instructions,

        discharge_status="DISCHARGED",

        status="ACTIVE",
    )

    summary = create_discharge_summary(
        db,
        new_summary,
    )

    ipd.status = "DISCHARGED"

    update_ipd(
        db,
        ipd,
    )

    if ipd.bed_id:

        bed = get_bed_by_id(
            db,
            ipd.bed_id,
        )

        if bed:

            bed.status = "AVAILABLE"

            update_bed(
                db,
                bed,
            )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DISCHARGE_SUMMARY",
        action="CREATE",
    )

    return summary


def get_all_discharge_summaries_service(
    db: Session,
    current_user: User,
):

    return get_all_discharge_summaries(
        db
    )


def get_discharge_summary_service(
    db: Session,
    discharge_summary_id: int,
    current_user: User,
):

    summary = get_discharge_summary_by_id(
        db,
        discharge_summary_id,
    )

    if summary is None:

        not_found(
            "Discharge Summary not found."
        )

    return summary


def update_discharge_summary_service(
    db: Session,
    discharge_summary_id: int,
    discharge_summary_update: DischargeSummaryUpdate,
    current_user: User,
):

    summary = get_discharge_summary_by_id(
        db,
        discharge_summary_id,
    )

    if summary is None:

        not_found(
            "Discharge Summary not found."
        )

    update_data = discharge_summary_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            summary,
            key,
            value,
        )

    updated = update_discharge_summary(
        db,
        summary,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DISCHARGE_SUMMARY",
        action="UPDATE",
    )

    return updated


def delete_discharge_summary_service(
    db: Session,
    discharge_summary_id: int,
    current_user: User,
):

    summary = get_discharge_summary_by_id(
        db,
        discharge_summary_id,
    )

    if summary is None:

        not_found(
            "Discharge Summary not found."
        )

    delete_discharge_summary(
        db,
        summary,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DISCHARGE_SUMMARY",
        action="DELETE",
    )

    return {
        "message": "Discharge Summary deleted successfully."
    }