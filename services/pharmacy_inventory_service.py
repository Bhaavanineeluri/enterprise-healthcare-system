from datetime import date

from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.pharmacy_inventory import PharmacyInventory
from models.user import User

from repositories.pharmacy_inventory_repository import (
    create_pharmacy_inventory,
    delete_pharmacy_inventory,
    get_all_pharmacy_inventory,
    get_pharmacy_inventory_by_batch,
    get_pharmacy_inventory_by_id,
    get_pharmacy_inventory_count,
    update_pharmacy_inventory,
)

from schemas.pharmacy_inventory_schema import (
    PharmacyInventoryCreate,
    PharmacyInventoryUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_pharmacy_inventory_code(
    db: Session,
):

    count = get_pharmacy_inventory_count(db)

    return f"PINV{count + 1:06d}"


def create_pharmacy_inventory_service(
    db: Session,
    inventory: PharmacyInventoryCreate,
    current_user: User,
):

    existing_batch = get_pharmacy_inventory_by_batch(
        db,
        inventory.batch_number,
    )

    if existing_batch:

        bad_request(
            "Batch number already exists."
        )

    if inventory.expiry_date <= date.today():

        bad_request(
            "Medicine expiry date must be in the future."
        )

    if inventory.quantity < 0:

        bad_request(
            "Quantity cannot be negative."
        )

    if inventory.minimum_stock < 0:

        bad_request(
            "Minimum stock cannot be negative."
        )

    if inventory.unit_price < 0:

        bad_request(
            "Unit price cannot be negative."
        )

    new_inventory = PharmacyInventory(

        pharmacy_inventory_code=generate_pharmacy_inventory_code(
            db,
        ),

        medicine_name=inventory.medicine_name,

        generic_name=inventory.generic_name,

        manufacturer=inventory.manufacturer,

        dosage_form=inventory.dosage_form,

        strength=inventory.strength,

        batch_number=inventory.batch_number,

        expiry_date=inventory.expiry_date,

        quantity=inventory.quantity,

        minimum_stock=inventory.minimum_stock,

        unit_price=inventory.unit_price,

        storage_location=inventory.storage_location,

        status="AVAILABLE",
    )

    inventory_data = create_pharmacy_inventory(
        db,
        new_inventory,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PHARMACY_INVENTORY",
        action="CREATE",
    )

    return inventory_data


def get_all_pharmacy_inventory_service(
    db: Session,
    current_user: User,
):

    return get_all_pharmacy_inventory(db)


def get_pharmacy_inventory_service(
    db: Session,
    inventory_id: int,
    current_user: User,
):

    inventory = get_pharmacy_inventory_by_id(
        db,
        inventory_id,
    )

    if inventory is None:

        not_found(
            "Inventory not found."
        )

    return inventory


def update_pharmacy_inventory_service(
    db: Session,
    inventory_id: int,
    inventory_update: PharmacyInventoryUpdate,
    current_user: User,
):

    inventory = get_pharmacy_inventory_by_id(
        db,
        inventory_id,
    )

    if inventory is None:

        not_found(
            "Inventory not found."
        )

    update_data = inventory_update.model_dump(
        exclude_unset=True,
    )

    if (
        "batch_number" in update_data
        and update_data["batch_number"] != inventory.batch_number
    ):

        existing = get_pharmacy_inventory_by_batch(
            db,
            update_data["batch_number"],
        )

        if existing:

            bad_request(
                "Batch number already exists."
            )

    if (
        "expiry_date" in update_data
        and update_data["expiry_date"] <= date.today()
    ):

        bad_request(
            "Expiry date must be in the future."
        )

    for field, value in update_data.items():

        setattr(
            inventory,
            field,
            value,
        )

    updated = update_pharmacy_inventory(
        db,
        inventory,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PHARMACY_INVENTORY",
        action="UPDATE",
    )

    return updated


def delete_pharmacy_inventory_service(
    db: Session,
    inventory_id: int,
    current_user: User,
):

    inventory = get_pharmacy_inventory_by_id(
        db,
        inventory_id,
    )

    if inventory is None:

        not_found(
            "Inventory not found."
        )

    delete_pharmacy_inventory(
        db,
        inventory,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PHARMACY_INVENTORY",
        action="DELETE",
    )

    return {
        "message": "Inventory deleted successfully."
    }