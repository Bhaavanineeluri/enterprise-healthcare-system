from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.patient import Patient
from models.user import User

from repositories.doctor_repository import (
    get_doctor_by_id,
)

from repositories.patient_repository import (
    create_patient,
    delete_patient,
    get_all_patients,
    get_patient_by_aadhaar,
    get_patient_by_email,
    get_patient_by_id,
    get_patient_by_phone,
    get_patient_count,
    update_patient,
)

from schemas.patient_schema import (
    PatientCreate,
    PatientUpdate,
)

from services.audit_service import save_audit_log


def generate_patient_code(
    db: Session,
):

    count = get_patient_count(db)

    return f"PAT{count + 1:06d}"


def create_patient_service(
    db: Session,
    patient: PatientCreate,
    current_user: User,
):

    if patient.doctor_id:

        doctor = get_doctor_by_id(
            db,
            patient.doctor_id,
        )

        if doctor is None:

            not_found(
                "Doctor not found."
            )

    if patient.email:

        existing = get_patient_by_email(
            db,
            patient.email,
        )

        if existing:

            bad_request(
                "Patient email already exists."
            )

    existing = get_patient_by_phone(
        db,
        patient.phone,
    )

    if existing:

        bad_request(
            "Patient phone already exists."
        )

    if patient.aadhaar_number:

        existing = get_patient_by_aadhaar(
            db,
            patient.aadhaar_number,
        )

        if existing:

            bad_request(
                "Aadhaar number already exists."
            )

    new_patient = Patient(

        patient_code=generate_patient_code(db),

        doctor_id=patient.doctor_id,

        first_name=patient.first_name,

        last_name=patient.last_name,

        gender=patient.gender,

        date_of_birth=patient.date_of_birth,

        blood_group=patient.blood_group,

        marital_status=patient.marital_status,

        phone=patient.phone,

        email=patient.email,

        address=patient.address,

        city=patient.city,

        state=patient.state,

        country=patient.country,

        postal_code=patient.postal_code,

        emergency_contact_name=patient.emergency_contact_name,

        emergency_contact_number=patient.emergency_contact_number,

        relationship_with_patient=patient.relationship_with_patient,

        aadhaar_number=patient.aadhaar_number,

        insurance_provider=patient.insurance_provider,

        insurance_policy_number=patient.insurance_policy_number,

        allergies=patient.allergies,

        medical_history=patient.medical_history,
    )

    patient_data = create_patient(
        db,
        new_patient,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PATIENT",
        action="CREATE",
    )

    return patient_data


def get_all_patients_service(
    db: Session,
    current_user: User,
):

    return get_all_patients(db)


def get_patient_service(
    db: Session,
    patient_id: int,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    return patient


def update_patient_service(
    db: Session,
    patient_id: int,
    patient_update: PatientUpdate,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    update_data = patient_update.model_dump(
        exclude_unset=True
    )

    if "doctor_id" in update_data:

        if update_data["doctor_id"] is not None:

            doctor = get_doctor_by_id(
                db,
                update_data["doctor_id"],
            )

            if doctor is None:

                not_found(
                    "Doctor not found."
                )

    if (
        "email" in update_data
        and
        update_data["email"] != patient.email
    ):

        existing = get_patient_by_email(
            db,
            update_data["email"],
        )

        if existing:

            bad_request(
                "Patient email already exists."
            )

    if (
        "phone" in update_data
        and
        update_data["phone"] != patient.phone
    ):

        existing = get_patient_by_phone(
            db,
            update_data["phone"],
        )

        if existing:

            bad_request(
                "Patient phone already exists."
            )

    if (
        "aadhaar_number" in update_data
        and
        update_data["aadhaar_number"] != patient.aadhaar_number
    ):

        existing = get_patient_by_aadhaar(
            db,
            update_data["aadhaar_number"],
        )

        if existing:

            bad_request(
                "Aadhaar number already exists."
            )

    for key, value in update_data.items():

        setattr(
            patient,
            key,
            value,
        )

    updated = update_patient(
        db,
        patient,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PATIENT",
        action="UPDATE",
    )

    return updated


def delete_patient_service(
    db: Session,
    patient_id: int,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    delete_patient(
        db,
        patient,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PATIENT",
        action="DELETE",
    )

    return {
        "message": "Patient deleted successfully."
    }