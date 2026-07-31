from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.drug_stock_management import DrugStockManagement
from models.user import User

from repositories.drug_stock_management_repository import (
    create_drug_stock_management,
    delete_drug_stock_management,
    get_all_drug_stock_management,
    get_drug_stock_management_by_id,
    get_drug_stock_management_count,
    update_drug_stock_management,
)

from repositories.pharmacy_inventory_repository import (
    get_pharmacy_inventory_by_id,
    update_pharmacy_inventory,
)

from schemas.drug_stock_management_schema import (
    DrugStockManagementCreate,
    DrugStockManagementUpdate,
)

from services.audit_service import (
    save_audit_log,
)


VALID_TRANSACTION_TYPES = {
    "STOCK_IN",
    "STOCK_OUT",
    "STOCK_ADJUSTMENT",
    "DAMAGED",
    "EXPIRED",
}


def generate_stock_code(
    db: Session,
):

    count = get_drug_stock_management_count(db)

    return f"DSTK{count + 1:06d}"


def update_inventory_status(
    inventory,
):

    if inventory.quantity <= 0:

        inventory.quantity = 0

        inventory.status = "OUT_OF_STOCK"

    elif inventory.quantity <= inventory.minimum_stock:

        inventory.status = "LOW_STOCK"

    else:

        inventory.status = "AVAILABLE"


def create_drug_stock_management_service(
    db: Session,
    stock: DrugStockManagementCreate,
    current_user: User,
):

    inventory = get_pharmacy_inventory_by_id(
        db,
        stock.pharmacy_inventory_id,
    )

    if inventory is None:

        not_found(
            "Inventory not found."
        )

    if stock.transaction_type not in VALID_TRANSACTION_TYPES:

        bad_request(
            "Invalid transaction type."
        )

    if stock.quantity <= 0:

        bad_request(
            "Quantity must be greater than zero."
        )

    previous_quantity = inventory.quantity

    if stock.transaction_type == "STOCK_IN":

        inventory.quantity += stock.quantity

    elif stock.transaction_type in (
        "STOCK_OUT",
        "DAMAGED",
        "EXPIRED",
    ):

        if inventory.quantity < stock.quantity:

            bad_request(
                "Insufficient stock available."
            )

        inventory.quantity -= stock.quantity

    elif stock.transaction_type == "STOCK_ADJUSTMENT":

        inventory.quantity = stock.quantity

    update_inventory_status(
        inventory,
    )

    update_pharmacy_inventory(
        db,
        inventory,
    )

    stock_record = DrugStockManagement(

        stock_code=generate_stock_code(
            db,
        ),

        pharmacy_inventory_id=stock.pharmacy_inventory_id,

        transaction_type=stock.transaction_type,

        quantity=stock.quantity,

        previous_quantity=previous_quantity,

        updated_quantity=inventory.quantity,

        remarks=stock.remarks,

        updated_by=stock.updated_by,

        updated_at=stock.updated_at,

        status="COMPLETED",
    )

    created = create_drug_stock_management(
        db,
        stock_record,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DRUG_STOCK_MANAGEMENT",
        action="CREATE",
    )

    return created


def get_all_drug_stock_management_service(
    db: Session,
    current_user: User,
):

    return get_all_drug_stock_management(db)


def get_drug_stock_management_service(
    db: Session,
    stock_id: int,
    current_user: User,
):

    stock = get_drug_stock_management_by_id(
        db,
        stock_id,
    )

    if stock is None:

        not_found(
            "Stock record not found."
        )

    return stock


def update_drug_stock_management_service(
    db: Session,
    stock_id: int,
    stock_update: DrugStockManagementUpdate,
    current_user: User,
):

    stock = get_drug_stock_management_by_id(
        db,
        stock_id,
    )

    if stock is None:

        not_found(
            "Stock record not found."
        )

    update_data = stock_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            stock,
            key,
            value,
        )

    updated = update_drug_stock_management(
        db,
        stock,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DRUG_STOCK_MANAGEMENT",
        action="UPDATE",
    )

    return updated


def delete_drug_stock_management_service(
    db: Session,
    stock_id: int,
    current_user: User,
):

    stock = get_drug_stock_management_by_id(
        db,
        stock_id,
    )

    if stock is None:

        not_found(
            "Stock record not found."
        )

    delete_drug_stock_management(
        db,
        stock,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DRUG_STOCK_MANAGEMENT",
        action="DELETE",
    )

    return {
        "message": "Drug Stock Management record deleted successfully."
    }