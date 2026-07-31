from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.hospital import Hospital
from models.user import User

from repositories.hospital_repository import (
    create_hospital,
    delete_hospital,
    get_all_hospitals,
    get_hospital_by_email,
    get_hospital_by_id,
    get_hospital_by_license_number,
    get_hospital_by_registration_number,
    get_hospital_count,
    update_hospital,
)

from schemas.hospital_schema import (
    HospitalCreate,
    HospitalUpdate,
)

from services.audit_service import save_audit_log


def generate_hospital_code(
    db: Session,
):

    count = get_hospital_count(db)

    return f"HSP{count + 1:06d}"


def create_hospital_service(
    db: Session,
    hospital: HospitalCreate,
    current_user: User,
):

    if get_hospital_by_email(
        db,
        hospital.email,
    ):

        bad_request(
        "Email already exists."
    )

    if get_hospital_by_registration_number(
        db,
        hospital.registration_number,
    ):

        raise HTTPException(
            status_code=400,
            detail="Registration number already exists."
        )

    if get_hospital_by_license_number(
        db,
        hospital.license_number,
    ):

        raise HTTPException(
            status_code=400,
            detail="License number already exists."
        )

    new_hospital = Hospital(

        hospital_code=generate_hospital_code(db),

        hospital_name=hospital.hospital_name,

        registration_number=hospital.registration_number,

        license_number=hospital.license_number,

        hospital_type=hospital.hospital_type,

        email=hospital.email,

        phone=hospital.phone,

        website=hospital.website,

        address=hospital.address,

        city=hospital.city,

        state=hospital.state,

        country=hospital.country,

        postal_code=hospital.postal_code,

        timezone=hospital.timezone,

        description=hospital.description,
    )

    hospital_data = create_hospital(
        db,
        new_hospital,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="HOSPITAL",
        action="CREATE",
    )

    return hospital_data


def get_all_hospitals_service(
    db: Session,
    current_user: User,
):

    return get_all_hospitals(db)


def get_hospital_service(
    db: Session,
    hospital_id: int,
    current_user: User,
):

    hospital = get_hospital_by_id(
        db,
        hospital_id,
    )

    if hospital is None:

        raise HTTPException(
            status_code=404,
            detail="Hospital not found."
        )

    return hospital


def update_hospital_service(
    db: Session,
    hospital_id: int,
    hospital_update: HospitalUpdate,
    current_user: User,
):

    hospital = get_hospital_by_id(
        db,
        hospital_id,
    )

    if hospital is None:

        raise HTTPException(
            status_code=404,
            detail="Hospital not found."
        )

    update_data = hospital_update.model_dump(
        exclude_unset=True
    )

    if (
        "email" in update_data
        and
        update_data["email"] != hospital.email
    ):

        existing = get_hospital_by_email(
            db,
            update_data["email"],
        )

        if existing:

            raise HTTPException(
                status_code=400,
                detail="Email already exists."
            )

    for key, value in update_data.items():

        setattr(
            hospital,
            key,
            value,
        )

    updated = update_hospital(
        db,
        hospital,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="HOSPITAL",
        action="UPDATE",
    )

    return updated


def delete_hospital_service(
    db: Session,
    hospital_id: int,
    current_user: User,
):

    hospital = get_hospital_by_id(
        db,
        hospital_id,
    )

    if hospital is None:

        raise HTTPException(
            status_code=404,
            detail="Hospital not found."
        )

    delete_hospital(
        db,
        hospital,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="HOSPITAL",
        action="DELETE",
    )

    return {
        "message": "Hospital deleted successfully."
    }