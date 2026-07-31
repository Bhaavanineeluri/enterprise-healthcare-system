from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.ambulance import Ambulance
from models.user import User

from repositories.ambulance_repository import (
    create_ambulance,
    delete_ambulance,
    get_all_ambulances,
    get_ambulance_by_id,
    get_ambulance_by_vehicle_number,
    get_ambulance_count,
    update_ambulance,
)

from schemas.ambulance_schema import (
    AmbulanceCreate,
    AmbulanceUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_ambulance_code(
    db: Session,
):

    count = get_ambulance_count(db)

    return f"AMB{count + 1:06d}"


def create_ambulance_service(
    db: Session,
    ambulance: AmbulanceCreate,
    current_user: User,
):

    existing = get_ambulance_by_vehicle_number(
        db,
        ambulance.vehicle_number,
    )

    if existing:

        bad_request(
            "Vehicle number already exists."
        )

    new_ambulance = Ambulance(

        ambulance_code=generate_ambulance_code(
            db
        ),

        vehicle_number=ambulance.vehicle_number,

        vehicle_type=ambulance.vehicle_type,

        driver_name=ambulance.driver_name,

        driver_phone=ambulance.driver_phone,

        current_location=ambulance.current_location,

        status="AVAILABLE",
    )

    ambulance_data = create_ambulance(
        db,
        new_ambulance,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="AMBULANCE",
        action="CREATE",
    )

    return ambulance_data


def get_all_ambulances_service(
    db: Session,
):

    return get_all_ambulances(db)


def get_ambulance_service(
    db: Session,
    ambulance_id: int,
    current_user: User,
):

    ambulance = get_ambulance_by_id(
        db,
        ambulance_id,
    )

    if ambulance is None:

        not_found(
            "Ambulance not found."
        )

    return ambulance


def update_ambulance_service(
    db: Session,
    ambulance_id: int,
    ambulance_update: AmbulanceUpdate,
    current_user: User,
):

    ambulance = get_ambulance_by_id(
        db,
        ambulance_id,
    )

    if ambulance is None:

        not_found(
            "Ambulance not found."
        )

    update_data = ambulance_update.model_dump(
        exclude_unset=True
    )

    if (
        "vehicle_number" in update_data
        and update_data["vehicle_number"] != ambulance.vehicle_number
    ):

        existing = get_ambulance_by_vehicle_number(
            db,
            update_data["vehicle_number"],
        )

        if existing:

            bad_request(
                "Vehicle number already exists."
            )

    for key, value in update_data.items():

        setattr(
            ambulance,
            key,
            value,
        )

    updated = update_ambulance(
        db,
        ambulance,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="AMBULANCE",
        action="UPDATE",
    )

    return updated


def delete_ambulance_service(
    db: Session,
    ambulance_id: int,
    current_user: User,
):

    ambulance = get_ambulance_by_id(
        db,
        ambulance_id,
    )

    if ambulance is None:

        not_found(
            "Ambulance not found."
        )

    delete_ambulance(
        db,
        ambulance,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="AMBULANCE",
        action="DELETE",
    )

    return {
        "message": "Ambulance deleted successfully."
    }