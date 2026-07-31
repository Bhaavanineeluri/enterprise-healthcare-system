from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.medicine_dispensing import MedicineDispensing
from models.user import User

from repositories.medicine_dispensing_repository import (
    create_medicine_dispensing,
    delete_medicine_dispensing,
    get_all_medicine_dispensings,
    get_medicine_dispensing_by_id,
    get_medicine_dispensing_count,
    update_medicine_dispensing,
)

from repositories.pharmacy_inventory_repository import (
    get_pharmacy_inventory_by_id,
    update_pharmacy_inventory,
)

from repositories.prescription_validation_repository import (
    get_prescription_validation_by_id,
)

from schemas.medicine_dispensing_schema import (
    MedicineDispensingCreate,
    MedicineDispensingUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_dispensing_code(
    db: Session,
):

    count = get_medicine_dispensing_count(db)

    return f"MDSP{count + 1:06d}"


def create_medicine_dispensing_service(
    db: Session,
    dispensing: MedicineDispensingCreate,
    current_user: User,
):

    validation = get_prescription_validation_by_id(
        db,
        dispensing.prescription_validation_id,
    )

    if validation is None:

        not_found(
            "Prescription Validation not found."
        )

    if validation.validation_status != "VALIDATED":

        bad_request(
            "Prescription has not been validated."
        )

    inventory = get_pharmacy_inventory_by_id(
        db,
        dispensing.pharmacy_inventory_id,
    )

    if inventory is None:

        not_found(
            "Inventory record not found."
        )

    if inventory.quantity < dispensing.dispensed_quantity:

        bad_request(
            "Insufficient stock available."
        )

    if dispensing.dispensed_quantity <= 0:

        bad_request(
            "Dispensed quantity must be greater than zero."
        )

    if dispensing.dispensed_quantity > validation.approved_quantity:

        bad_request(
            "Dispensed quantity exceeds approved quantity."
        )

    inventory.quantity -= dispensing.dispensed_quantity

    if inventory.quantity == 0:

        inventory.status = "OUT_OF_STOCK"

    elif inventory.quantity <= inventory.minimum_stock:

        inventory.status = "LOW_STOCK"

    else:

        inventory.status = "AVAILABLE"

    update_pharmacy_inventory(
        db,
        inventory,
    )

    new_dispensing = MedicineDispensing(

        dispensing_code=generate_dispensing_code(
            db,
        ),

        prescription_validation_id=dispensing.prescription_validation_id,

        pharmacy_inventory_id=dispensing.pharmacy_inventory_id,

        dispensed_quantity=dispensing.dispensed_quantity,

        dispensed_by=dispensing.dispensed_by,

        dispensed_at=dispensing.dispensed_at,

        remarks=dispensing.remarks,

        status="DISPENSED",
    )

    dispensing_data = create_medicine_dispensing(
        db,
        new_dispensing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="MEDICINE_DISPENSING",
        action="CREATE",
    )

    return dispensing_data


def get_all_medicine_dispensings_service(
    db: Session,
    current_user: User,
):

    return get_all_medicine_dispensings(db)


def get_medicine_dispensing_service(
    db: Session,
    dispensing_id: int,
    current_user: User,
):

    dispensing = get_medicine_dispensing_by_id(
        db,
        dispensing_id,
    )

    if dispensing is None:

        not_found(
            "Medicine Dispensing not found."
        )

    return dispensing


def update_medicine_dispensing_service(
    db: Session,
    dispensing_id: int,
    dispensing_update: MedicineDispensingUpdate,
    current_user: User,
):

    dispensing = get_medicine_dispensing_by_id(
        db,
        dispensing_id,
    )

    if dispensing is None:

        not_found(
            "Medicine Dispensing not found."
        )

    update_data = dispensing_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            dispensing,
            key,
            value,
        )

    updated = update_medicine_dispensing(
        db,
        dispensing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="MEDICINE_DISPENSING",
        action="UPDATE",
    )

    return updated


def delete_medicine_dispensing_service(
    db: Session,
    dispensing_id: int,
    current_user: User,
):

    dispensing = get_medicine_dispensing_by_id(
        db,
        dispensing_id,
    )

    if dispensing is None:

        not_found(
            "Medicine Dispensing not found."
        )

    delete_medicine_dispensing(
        db,
        dispensing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="MEDICINE_DISPENSING",
        action="DELETE",
    )

    return {
        "message": "Medicine Dispensing deleted successfully."
    }