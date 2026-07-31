from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.diagnosis import Diagnosis
from models.user import User

from repositories.diagnosis_repository import (
    create_diagnosis,
    delete_diagnosis,
    get_all_diagnosis,
    get_diagnosis_by_id,
    get_diagnosis_count,
    update_diagnosis,
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

from schemas.diagnosis_schema import (
    DiagnosisCreate,
    DiagnosisUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_diagnosis_code(
    db: Session,
):

    count = get_diagnosis_count(db)

    return f"DGN{count + 1:06d}"


def create_diagnosis_service(
    db: Session,
    diagnosis: DiagnosisCreate,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        diagnosis.emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    patient = get_patient_by_id(
        db,
        diagnosis.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        diagnosis.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    new_diagnosis = Diagnosis(

        diagnosis_code=generate_diagnosis_code(
            db
        ),

        emr_id=diagnosis.emr_id,

        patient_id=diagnosis.patient_id,

        doctor_id=diagnosis.doctor_id,

        diagnosis_name=diagnosis.diagnosis_name,

        diagnosis_type=diagnosis.diagnosis_type,

        icd10_code=diagnosis.icd10_code,

        description=diagnosis.description,

        status="ACTIVE",
    )

    diagnosis_data = create_diagnosis(
        db,
        new_diagnosis,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DIAGNOSIS",
        action="CREATE",
    )

    return diagnosis_data


def get_all_diagnosis_service(
    db: Session,
    current_user: User,
):

    return get_all_diagnosis(
        db
    )


def get_diagnosis_service(
    db: Session,
    diagnosis_id: int,
    current_user: User,
):

    diagnosis = get_diagnosis_by_id(
        db,
        diagnosis_id,
    )

    if diagnosis is None:

        not_found(
            "Diagnosis not found."
        )

    return diagnosis


def update_diagnosis_service(
    db: Session,
    diagnosis_id: int,
    diagnosis_update: DiagnosisUpdate,
    current_user: User,
):

    diagnosis = get_diagnosis_by_id(
        db,
        diagnosis_id,
    )

    if diagnosis is None:

        not_found(
            "Diagnosis not found."
        )

    update_data = diagnosis_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            diagnosis,
            key,
            value,
        )

    updated = update_diagnosis(
        db,
        diagnosis,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DIAGNOSIS",
        action="UPDATE",
    )

    return updated


def delete_diagnosis_service(
    db: Session,
    diagnosis_id: int,
    current_user: User,
):

    diagnosis = get_diagnosis_by_id(
        db,
        diagnosis_id,
    )

    if diagnosis is None:

        not_found(
            "Diagnosis not found."
        )

    delete_diagnosis(
        db,
        diagnosis,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DIAGNOSIS",
        action="DELETE",
    )

    return {
        "message": "Diagnosis deleted successfully."
    }