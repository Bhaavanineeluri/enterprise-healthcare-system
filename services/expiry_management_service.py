from datetime import date, timedelta

from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.expiry_management import ExpiryManagement
from models.user import User

from repositories.expiry_management_repository import (
    create_expiry_management,
    delete_expiry_management,
    get_all_expiry_management,
    get_expiry_management_by_id,
    get_expiry_management_count,
    update_expiry_management,
)

from repositories.pharmacy_inventory_repository import (
    get_pharmacy_inventory_by_id,
)

from schemas.expiry_management_schema import (
    ExpiryManagementCreate,
    ExpiryManagementUpdate,
)

from services.audit_service import (
    save_audit_log,
)


NEAR_EXPIRY_DAYS = 30


def generate_expiry_code(
    db: Session,
):

    count = get_expiry_management_count(db)

    return f"EXPM{count + 1:06d}"


def calculate_expiry_status(
    expiry_date: date,
):

    today = date.today()

    if expiry_date < today:

        return "EXPIRED"

    if expiry_date <= today + timedelta(days=NEAR_EXPIRY_DAYS):

        return "NEAR_EXPIRY"

    return "VALID"


def create_expiry_management_service(
    db: Session,
    expiry: ExpiryManagementCreate,
    current_user: User,
):

    inventory = get_pharmacy_inventory_by_id(
        db,
        expiry.pharmacy_inventory_id,
    )

    if inventory is None:

        not_found(
            "Pharmacy Inventory not found."
        )

    expiry_status = calculate_expiry_status(
        inventory.expiry_date,
    )

    new_expiry = ExpiryManagement(

        expiry_code=generate_expiry_code(
            db,
        ),

        pharmacy_inventory_id=expiry.pharmacy_inventory_id,

        review_date=expiry.review_date,

        expiry_status=expiry_status,

        reviewed_by=expiry.reviewed_by,

        remarks=expiry.remarks,
    )

    created = create_expiry_management(
        db,
        new_expiry,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EXPIRY_MANAGEMENT",
        action="CREATE",
    )

    return created


def get_all_expiry_management_service(
    db: Session,
    current_user: User,
):

    return get_all_expiry_management(
        db,
    )


def get_expiry_management_service(
    db: Session,
    expiry_id: int,
    current_user: User,
):

    expiry = get_expiry_management_by_id(
        db,
        expiry_id,
    )

    if expiry is None:

        not_found(
            "Expiry record not found."
        )

    return expiry


def update_expiry_management_service(
    db: Session,
    expiry_id: int,
    expiry_update: ExpiryManagementUpdate,
    current_user: User,
):

    expiry = get_expiry_management_by_id(
        db,
        expiry_id,
    )

    if expiry is None:

        not_found(
            "Expiry record not found."
        )

    update_data = expiry_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            expiry,
            key,
            value,
        )

    updated = update_expiry_management(
        db,
        expiry,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EXPIRY_MANAGEMENT",
        action="UPDATE",
    )

    return updated


def delete_expiry_management_service(
    db: Session,
    expiry_id: int,
    current_user: User,
):

    expiry = get_expiry_management_by_id(
        db,
        expiry_id,
    )

    if expiry is None:

        not_found(
            "Expiry record not found."
        )

    delete_expiry_management(
        db,
        expiry,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="EXPIRY_MANAGEMENT",
        action="DELETE",
    )

    return {
        "message": "Expiry Management deleted successfully."
    }