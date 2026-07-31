from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.user import User
from models.ward import Ward

from repositories.branch_repository import (
    get_branch_by_id,
)

from repositories.ward_repository import (
    create_ward,
    delete_ward,
    get_all_wards,
    get_ward_by_code,
    get_ward_by_id,
    get_ward_count,
    update_ward,
)

from schemas.ward_schema import (
    WardCreate,
    WardUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_ward_code(
    db: Session,
):

    count = get_ward_count(db)

    return f"WRD{count + 1:06d}"


def create_ward_service(
    db: Session,
    ward: WardCreate,
    current_user: User,
):

    branch = get_branch_by_id(
        db,
        ward.branch_id,
    )

    if branch is None:

        not_found(
            "Branch not found."
        )

    new_ward = Ward(

        ward_code=generate_ward_code(db),

        branch_id=ward.branch_id,

        ward_name=ward.ward_name,

        ward_type=ward.ward_type,

        floor=ward.floor,

        capacity=ward.capacity,

        occupied_beds=0,

        incharge_name=ward.incharge_name,

        phone=ward.phone,

        description=ward.description,
    )

    ward_data = create_ward(
        db,
        new_ward,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="WARD",
        action="CREATE",
    )

    return ward_data


def get_all_wards_service(
    db: Session,
    current_user: User,
):

    return get_all_wards(
        db
    )


def get_ward_service(
    db: Session,
    ward_id: int,
    current_user: User,
):

    ward = get_ward_by_id(
        db,
        ward_id,
    )

    if ward is None:

        not_found(
            "Ward not found."
        )

    return ward


def update_ward_service(
    db: Session,
    ward_id: int,
    ward_update: WardUpdate,
    current_user: User,
):

    ward = get_ward_by_id(
        db,
        ward_id,
    )

    if ward is None:

        not_found(
            "Ward not found."
        )

    update_data = ward_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        setattr(
            ward,
            key,
            value,
        )

    updated = update_ward(
        db,
        ward,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="WARD",
        action="UPDATE",
    )

    return updated


def delete_ward_service(
    db: Session,
    ward_id: int,
    current_user: User,
):

    ward = get_ward_by_id(
        db,
        ward_id,
    )

    if ward is None:

        not_found(
            "Ward not found."
        )

    delete_ward(
        db,
        ward,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="WARD",
        action="DELETE",
    )

    return {
        "message": "Ward deleted successfully."
    }