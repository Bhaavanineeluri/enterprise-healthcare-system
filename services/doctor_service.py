from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.doctor import Doctor
from models.user import User

from repositories.department_repository import (
    get_department_by_id,
)

from repositories.doctor_repository import (
    create_doctor,
    delete_doctor,
    get_all_doctors,
    get_doctor_by_email,
    get_doctor_by_id,
    get_doctor_by_license,
    get_doctor_count,
    update_doctor,
)

from schemas.doctor_schema import (
    DoctorCreate,
    DoctorUpdate,
)

from services.audit_service import save_audit_log


def generate_doctor_code(
    db: Session,
):

    count = get_doctor_count(db)

    return f"DOC{count + 1:06d}"


def create_doctor_service(
    db: Session,
    doctor: DoctorCreate,
    current_user: User,
):

    department = get_department_by_id(
        db,
        doctor.department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    if get_doctor_by_email(
        db,
        doctor.email,
    ):

        bad_request(
            "Doctor email already exists."
        )

    if get_doctor_by_license(
        db,
        doctor.license_number,
    ):

        bad_request(
            "License number already exists."
        )

    new_doctor = Doctor(

        doctor_code=generate_doctor_code(db),

        department_id=doctor.department_id,

        first_name=doctor.first_name,

        last_name=doctor.last_name,

        gender=doctor.gender,

        specialization=doctor.specialization,

        qualification=doctor.qualification,

        license_number=doctor.license_number,

        experience=doctor.experience,

        email=doctor.email,

        phone=doctor.phone,

        consultation_fee=doctor.consultation_fee,
    )

    doctor_data = create_doctor(
        db,
        new_doctor,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DOCTOR",
        action="CREATE",
    )

    return doctor_data


def get_all_doctors_service(
    db: Session,
    current_user: User,
):

    return get_all_doctors(db)


def get_doctor_service(
    db: Session,
    doctor_id: int,
    current_user: User,
):

    doctor = get_doctor_by_id(
        db,
        doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    return doctor


def update_doctor_service(
    db: Session,
    doctor_id: int,
    doctor_update: DoctorUpdate,
    current_user: User,
):

    doctor = get_doctor_by_id(
        db,
        doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    update_data = doctor_update.model_dump(
        exclude_unset=True
    )

    if (
        "department_id" in update_data
    ):

        department = get_department_by_id(
            db,
            update_data["department_id"],
        )

        if department is None:

            not_found(
                "Department not found."
            )

    if (
        "email" in update_data
        and
        update_data["email"] != doctor.email
    ):

        existing = get_doctor_by_email(
            db,
            update_data["email"],
        )

        if existing:

            bad_request(
                "Doctor email already exists."
            )

    if (
        "license_number" in update_data
        and
        update_data["license_number"] != doctor.license_number
    ):

        existing = get_doctor_by_license(
            db,
            update_data["license_number"],
        )

        if existing:

            bad_request(
                "License number already exists."
            )

    for key, value in update_data.items():

        setattr(
            doctor,
            key,
            value,
        )

    updated = update_doctor(
        db,
        doctor,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DOCTOR",
        action="UPDATE",
    )

    return updated


def delete_doctor_service(
    db: Session,
    doctor_id: int,
    current_user: User,
):

    doctor = get_doctor_by_id(
        db,
        doctor_id,
    )

    if doctor is None:

        not_found(
            "Doctor not found."
        )

    delete_doctor(
        db,
        doctor,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DOCTOR",
        action="DELETE",
    )

    return {
        "message": "Doctor deleted successfully."
    }