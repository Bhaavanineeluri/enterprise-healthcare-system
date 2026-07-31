from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.opd import OPD
from models.user import User

from repositories.opd_repository import (
    create_opd,
    delete_opd,
    get_all_opd,
    get_opd_by_appointment,
    get_opd_by_id,
    get_opd_count,
    get_next_token_number,
    update_opd,
)

from repositories.appointment_repository import (
    get_appointment_by_id,
    update_appointment,
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

from schemas.opd_schema import (
    OPDCreate,
    OPDUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_opd_code(
    db: Session,
):

    count = get_opd_count(db)

    return f"OPD{count + 1:06d}"


def create_opd_service(
    db: Session,
    opd: OPDCreate,
    current_user: User,
):

    appointment = get_appointment_by_id(
        db,
        opd.appointment_id,
    )

    if appointment is None:

        not_found(
            "Appointment not found."
        )

    existing = get_opd_by_appointment(
        db,
        opd.appointment_id,
    )

    if existing:

        bad_request(
            "OPD already created for this appointment."
        )

    patient = get_patient_by_id(
        db,
        opd.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    doctor = get_doctor_by_id(
        db,
        opd.doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    department = get_department_by_id(
        db,
        opd.department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    new_opd = OPD(

        opd_code=generate_opd_code(
            db
        ),

        appointment_id=opd.appointment_id,

        patient_id=opd.patient_id,

        doctor_id=opd.doctor_id,

        department_id=opd.department_id,

        visit_datetime=opd.visit_datetime,

        token_number=get_next_token_number(
            db
        ),

        height=opd.height,

        weight=opd.weight,

        bmi=opd.bmi,

        temperature=opd.temperature,

        pulse=opd.pulse,

        blood_pressure=opd.blood_pressure,

        oxygen_saturation=opd.oxygen_saturation,

        notes=opd.notes,

        status="WAITING",
    )

    opd_data = create_opd(
        db,
        new_opd,
    )

    appointment.status = "COMPLETED"

    update_appointment(
        db,
        appointment,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="OPD",
        action="CREATE",
    )

    return opd_data


def get_all_opd_service(
    db: Session,
    current_user: User,
):

    return get_all_opd(
        db
    )


def get_opd_service(
    db: Session,
    opd_id: int,
    current_user: User,
):

    opd = get_opd_by_id(
        db,
        opd_id,
    )

    if opd is None:

        not_found(
            "OPD record not found."
        )

    return opd


def update_opd_service(
    db: Session,
    opd_id: int,
    opd_update: OPDUpdate,
    current_user: User,
):

    opd = get_opd_by_id(
        db,
        opd_id,
    )

    if opd is None:

        not_found(
            "OPD record not found."
        )

    update_data = opd_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            opd,
            key,
            value,
        )

    updated = update_opd(
        db,
        opd,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="OPD",
        action="UPDATE",
    )

    return updated


def delete_opd_service(
    db: Session,
    opd_id: int,
    current_user: User,
):

    opd = get_opd_by_id(
        db,
        opd_id,
    )

    if opd is None:

        not_found(
            "OPD record not found."
        )

    delete_opd(
        db,
        opd,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="OPD",
        action="DELETE",
    )

    return {
        "message": "OPD record deleted successfully."
    }