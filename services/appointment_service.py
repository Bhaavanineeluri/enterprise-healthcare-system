from datetime import datetime

from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)
from datetime import datetime, timezone
from models.appointment import Appointment
from models.user import User

from repositories.appointment_repository import (
    create_appointment,
    get_all_appointments,
    get_appointment_by_id,
    get_appointment_count,
    get_doctor_appointment,
    update_appointment,
    delete_appointment,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from repositories.doctor_repository import (
    get_doctor_by_id,
)

from repositories.department_repository import (
    get_department_by_id,
)

from services.audit_service import (
    save_audit_log,
)

from schemas.appointment_schema import (
    AppointmentCreate,
    AppointmentUpdate,
)


def generate_appointment_code(
    db: Session,
):

    count = get_appointment_count(db)

    return f"APT{count + 1:06d}"

def create_appointment_service(
    db: Session,
    appointment: AppointmentCreate,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        appointment.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        appointment.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    department = get_department_by_id(
        db,
        appointment.department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    if appointment.appointment_datetime < datetime.now(timezone.utc):

        bad_request(
            "Appointment date cannot be in the past."
        )

    existing = get_doctor_appointment(
        db,
        appointment.doctor_id,
        appointment.appointment_datetime,
    )

    if existing:

        bad_request(
            "Doctor already has an appointment at this time."
        )

    new_appointment = Appointment(

        appointment_code=generate_appointment_code(
            db
        ),

        patient_id=appointment.patient_id,

        doctor_id=appointment.doctor_id,

        department_id=appointment.department_id,

        appointment_datetime=appointment.appointment_datetime,

        appointment_type=appointment.appointment_type,

        chief_complaint=appointment.chief_complaint,

        notes=appointment.notes,

        status="SCHEDULED",
    )

    appointment_data = create_appointment(
        db,
        new_appointment,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="APPOINTMENT",
        action="CREATE",
    )

    return appointment_data

def get_all_appointments_service(
    db: Session,
    current_user: User,
):

    return get_all_appointments(
        db
    )


def get_appointment_service(
    db: Session,
    appointment_id: int,
    current_user: User,
):

    appointment = get_appointment_by_id(
        db,
        appointment_id,
    )

    if appointment is None:

        not_found(
            "Appointment not found."
        )

    return appointment


def update_appointment_service(
    db: Session,
    appointment_id: int,
    appointment_update: AppointmentUpdate,
    current_user: User,
):

    appointment = get_appointment_by_id(
        db,
        appointment_id,
    )

    if appointment is None:

        not_found(
            "Appointment not found."
        )

    update_data = appointment_update.model_dump(
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

    if (
        "department_id" in update_data
        and update_data["department_id"] is not None
    ):

        department = get_department_by_id(
            db,
            update_data["department_id"],
        )

        if department is None:

            not_found(
                "Department not found."
            )

    if "appointment_datetime" in update_data:
        
        appointment_datetime = update_data["appointment_datetime"]

        if appointment_datetime.tzinfo is not None:

            appointment_datetime = appointment_datetime.replace(
                tzinfo=None
            )

        if appointment_datetime < datetime.now():

            bad_request(
                "Appointment date cannot be in the past."
            )

        update_data["appointment_datetime"] = appointment_datetime

    for key, value in update_data.items():

        setattr(
            appointment,
            key,
            value,
        )

    updated = update_appointment(
        db,
        appointment,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="APPOINTMENT",
        action="UPDATE",
    )

    return updated


def delete_appointment_service(
    db: Session,
    appointment_id: int,
    current_user: User,
):

    appointment = get_appointment_by_id(
        db,
        appointment_id,
    )

    if appointment is None:

        not_found(
            "Appointment not found."
        )

    delete_appointment(
        db,
        appointment,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="APPOINTMENT",
        action="DELETE",
    )

    return {
        "message": "Appointment deleted successfully."
    }