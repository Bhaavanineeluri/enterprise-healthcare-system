from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.emergency import Emergency
from models.user import User

from repositories.doctor_repository import (
    get_doctor_by_id,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from repositories.emergency_repository import (
    create_emergency,
    delete_emergency,
    get_all_emergencies,
    get_emergency_by_id,
    get_emergency_count,
    update_emergency,
)

from schemas.emergency_schema import (
    EmergencyCreate,
    EmergencyUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_emergency_code(
    db: Session,
):

    count = get_emergency_count(db)

    return f"EMG{count + 1:06d}"


def create_emergency_service(
    db: Session,
    emergency: EmergencyCreate,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        emergency.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    if emergency.doctor_id:

        doctor = get_doctor_by_id(
            db,
            emergency.doctor_id,
        )

        if doctor is None:

            not_found(
                "Doctor not found."
            )

    new_emergency = Emergency(

        emergency_code=generate_emergency_code(
            db
        ),

        patient_id=emergency.patient_id,

        doctor_id=emergency.doctor_id,

        emergency_type=emergency.emergency_type,

        priority=emergency.priority,

        arrival_time=emergency.arrival_time,

        symptoms=emergency.symptoms,

        diagnosis=emergency.diagnosis,

        treatment=emergency.treatment,

        remarks=emergency.remarks,

        status="OPEN",
    )

    emergency_data = create_emergency(
        db,
        new_emergency,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EMERGENCY",
        action="CREATE",
    )

    return emergency_data


def get_all_emergencies_service(
    db: Session,
    current_user: User,
):

    return get_all_emergencies(
        db
    )


def get_emergency_service(
    db: Session,
    emergency_id: int,
    current_user: User,
):

    emergency = get_emergency_by_id(
        db,
        emergency_id,
    )

    if emergency is None:

        not_found(
            "Emergency not found."
        )

    return emergency


def update_emergency_service(
    db: Session,
    emergency_id: int,
    emergency_update: EmergencyUpdate,
    current_user: User,
):

    emergency = get_emergency_by_id(
        db,
        emergency_id,
    )

    if emergency is None:

        not_found(
            "Emergency not found."
        )

    update_data = emergency_update.model_dump(
        exclude_unset=True
    )

    if (
        "doctor_id" in update_data
        and update_data["doctor_id"] is not None
    ):

        doctor = get_doctor_by_id(
            db,
            update_data["doctor_id"],
        )

        if doctor is None:

            not_found(
                "Doctor not found."
            )

    for key, value in update_data.items():

        setattr(
            emergency,
            key,
            value,
        )

    updated = update_emergency(
        db,
        emergency,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EMERGENCY",
        action="UPDATE",
    )

    return updated


def delete_emergency_service(
    db: Session,
    emergency_id: int,
    current_user: User,
):

    emergency = get_emergency_by_id(
        db,
        emergency_id,
    )

    if emergency is None:

        not_found(
            "Emergency not found."
        )

    delete_emergency(
        db,
        emergency,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EMERGENCY",
        action="DELETE",
    )

    return {
        "message": "Emergency deleted successfully."
    }