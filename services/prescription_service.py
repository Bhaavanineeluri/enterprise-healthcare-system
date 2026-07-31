from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.prescription import Prescription
from models.user import User

from repositories.prescription_repository import (
    create_prescription,
    delete_prescription,
    get_all_prescriptions,
    get_prescription_by_id,
    get_prescription_count,
    update_prescription,
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

from schemas.prescription_schema import (
    PrescriptionCreate,
    PrescriptionUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_prescription_code(
    db: Session,
):

    count = get_prescription_count(db)

    return f"PRS{count + 1:06d}"


def create_prescription_service(
    db: Session,
    prescription: PrescriptionCreate,
    current_user: User,
):

    emr = get_emr_by_id(
        db,
        prescription.emr_id,
    )

    if emr is None:

        not_found(
            "EMR not found."
        )

    patient = get_patient_by_id(
        db,
        prescription.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        prescription.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    new_prescription = Prescription(

        prescription_code=generate_prescription_code(
            db
        ),

        emr_id=prescription.emr_id,

        patient_id=prescription.patient_id,

        doctor_id=prescription.doctor_id,

        medicine_name=prescription.medicine_name,

        dosage=prescription.dosage,

        frequency=prescription.frequency,

        duration=prescription.duration,

        instructions=prescription.instructions,

        status="ACTIVE",
    )

    prescription_data = create_prescription(
        db,
        new_prescription,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PRESCRIPTION",
        action="CREATE",
    )

    return prescription_data


def get_all_prescriptions_service(
    db: Session,
    current_user: User,
):

    return get_all_prescriptions(
        db
    )


def get_prescription_service(
    db: Session,
    prescription_id: int,
    current_user: User,
):

    prescription = get_prescription_by_id(
        db,
        prescription_id,
    )

    if prescription is None:

        not_found(
            "Prescription not found."
        )

    return prescription


def update_prescription_service(
    db: Session,
    prescription_id: int,
    prescription_update: PrescriptionUpdate,
    current_user: User,
):

    prescription = get_prescription_by_id(
        db,
        prescription_id,
    )

    if prescription is None:

        not_found(
            "Prescription not found."
        )

    update_data = prescription_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            prescription,
            key,
            value,
        )

    updated = update_prescription(
        db,
        prescription,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PRESCRIPTION",
        action="UPDATE",
    )

    return updated


def delete_prescription_service(
    db: Session,
    prescription_id: int,
    current_user: User,
):

    prescription = get_prescription_by_id(
        db,
        prescription_id,
    )

    if prescription is None:

        not_found(
            "Prescription not found."
        )

    delete_prescription(
        db,
        prescription,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PRESCRIPTION",
        action="DELETE",
    )

    return {
        "message": "Prescription deleted successfully."
    }