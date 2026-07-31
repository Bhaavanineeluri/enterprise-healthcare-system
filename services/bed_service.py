from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.bed import Bed
from models.user import User

from repositories.bed_repository import (
    create_bed,
    delete_bed,
    get_all_beds,
    get_bed_by_id,
    get_bed_by_number,
    get_bed_count,
    update_bed,
)
from repositories.room_repository import (
    get_room_by_id,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from schemas.bed_schema import (
    BedCreate,
    BedUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_bed_code(
    db: Session,
):

    count = get_bed_count(db)

    return f"BED{count + 1:06d}"


def create_bed_service(
    db: Session,
    bed: BedCreate,
    current_user: User,
):

    room = get_room_by_id(
        db,
        bed.room_id,
    )

    if room is None:

        not_found(
            "Room not found."
        )

    existing = get_bed_by_number(
        db,
        bed.bed_number,
    )

    if existing:

        bad_request(
            "Bed number already exists."
        )

    new_bed = Bed(

        bed_code=generate_bed_code(
            db
        ),

        room_id=bed.room_id,

        bed_number=bed.bed_number,

        bed_type=bed.bed_type,

        bed_status="AVAILABLE",
    )

    bed_data = create_bed(
        db,
        new_bed,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BED",
        action="CREATE",
    )

    return bed_data


def get_all_beds_service(
    db: Session,
    current_user: User,
):

    return get_all_beds(
        db
    )


def get_bed_service(
    db: Session,
    bed_id: int,
    current_user: User,
):

    bed = get_bed_by_id(
        db,
        bed_id,
    )

    if bed is None:

        not_found(
            "Bed not found."
        )

    return bed


def update_bed_service(
    db: Session,
    bed_id: int,
    bed_update: BedUpdate,
    current_user: User,
):

    bed = get_bed_by_id(
        db,
        bed_id,
    )

    if bed is None:

        not_found(
            "Bed not found."
        )

    update_data = bed_update.model_dump(
        exclude_unset=True
    )

    if "room_id" in update_data:

        room = get_room_by_id(
            db,
            update_data["room_id"],
        )

        if room is None:

            not_found(
                "Room not found."
            )

    if (
        "patient_id" in update_data
        and update_data["patient_id"] is not None
    ):

        patient = get_patient_by_id(
            db,
            update_data["patient_id"],
        )

        if patient is None:

            not_found(
                "Patient not found."
            )

    if (
        "bed_number" in update_data
        and update_data["bed_number"] != bed.bed_number
    ):

        existing = get_bed_by_number(
            db,
            update_data["bed_number"],
        )

        if existing:

            bad_request(
                "Bed number already exists."
            )

    for key, value in update_data.items():

        setattr(
            bed,
            key,
            value,
        )

    updated = update_bed(
        db,
        bed,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BED",
        action="UPDATE",
    )

    return updated


def delete_bed_service(
    db: Session,
    bed_id: int,
    current_user: User,
):

    bed = get_bed_by_id(
        db,
        bed_id,
    )

    if bed is None:

        not_found(
            "Bed not found."
        )

    delete_bed(
        db,
        bed,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BED",
        action="DELETE",
    )

    return {
        "message": "Bed deleted successfully."
    }