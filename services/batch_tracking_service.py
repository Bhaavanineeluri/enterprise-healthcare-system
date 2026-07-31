from datetime import date

from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.batch_tracking import BatchTracking
from models.user import User

from repositories.batch_tracking_repository import (
    create_batch_tracking,
    delete_batch_tracking,
    get_all_batch_tracking,
    get_batch_tracking_by_id,
    get_batch_tracking_count,
    update_batch_tracking,
)
from repositories.pharmacy_inventory_repository import (
    get_pharmacy_inventory_by_id,
)
from schemas.batch_tracking_schema import (
    BatchTrackingCreate,
    BatchTrackingUpdate,
)
from services.audit_service import (
    save_audit_log,
)

VALID_RECALL_STATUS = {
    "NOT_RECALLED",
    "RECALLED",
}
def generate_batch_tracking_code(
    db: Session,
):

    count = get_batch_tracking_count(db)

    return f"BTRK{count + 1:06d}"


def create_batch_tracking_service(
    db: Session,
    batch: BatchTrackingCreate,
    current_user: User,
):

    inventory = get_pharmacy_inventory_by_id(
        db,
        batch.pharmacy_inventory_id,
    )

    if inventory is None:

        not_found(
            "Pharmacy Inventory not found."
        )

    if batch.manufacturing_date > date.today():

        bad_request(
            "Manufacturing date cannot be in the future."
        )

    if batch.manufacturing_date >= inventory.expiry_date:

        bad_request(
            "Manufacturing date must be before expiry date."
        )

    if batch.recall_status not in VALID_RECALL_STATUS:

        bad_request(
            "Invalid recall status."
        )

    new_batch = BatchTracking(

        batch_tracking_code=generate_batch_tracking_code(
            db,
        ),

        pharmacy_inventory_id=batch.pharmacy_inventory_id,

        manufacturing_date=batch.manufacturing_date,

        recall_status=batch.recall_status,

        manufacturer=batch.manufacturer,

        remarks=batch.remarks,

        status="ACTIVE",
    )

    created = create_batch_tracking(
        db,
        new_batch,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BATCH_TRACKING",
        action="CREATE",
    )

    return created


def get_all_batch_tracking_service(
    db: Session,
    current_user: User,
):

    return get_all_batch_tracking(db)


def get_batch_tracking_service(
    db: Session,
    batch_id: int,
    current_user: User,
):

    batch = get_batch_tracking_by_id(
        db,
        batch_id,
    )

    if batch is None:

        not_found(
            "Batch Tracking record not found."
        )

    return batch


def update_batch_tracking_service(
    db: Session,
    batch_id: int,
    batch_update: BatchTrackingUpdate,
    current_user: User,
):

    batch = get_batch_tracking_by_id(
        db,
        batch_id,
    )

    if batch is None:

        not_found(
            "Batch Tracking record not found."
        )

    update_data = batch_update.model_dump(
        exclude_unset=True,
    )

    if (
        "recall_status" in update_data
        and update_data["recall_status"] not in VALID_RECALL_STATUS
    ):

        bad_request(
            "Invalid recall status."
        )

    for key, value in update_data.items():

        setattr(
            batch,
            key,
            value,
        )

    updated = update_batch_tracking(
        db,
        batch,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BATCH_TRACKING",
        action="UPDATE",
    )

    return updated


def delete_batch_tracking_service(
    db: Session,
    batch_id: int,
    current_user: User,
):

    batch = get_batch_tracking_by_id(
        db,
        batch_id,
    )

    if batch is None:

        not_found(
            "Batch Tracking record not found."
        )

    delete_batch_tracking(
        db,
        batch,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BATCH_TRACKING",
        action="DELETE",
    )

    return {
        "message": "Batch Tracking deleted successfully."
    }