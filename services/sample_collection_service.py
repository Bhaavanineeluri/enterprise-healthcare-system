from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.sample_collection import SampleCollection
from models.user import User

from repositories.sample_collection_repository import (
    create_sample_collection,
    delete_sample_collection,
    get_all_sample_collections,
    get_sample_collection_by_id,
    get_sample_collection_count,
    update_sample_collection,
)

from repositories.lab_order_repository import (
    get_lab_order_by_id,
    update_lab_order,
)

from schemas.sample_collection_schema import (
    SampleCollectionCreate,
    SampleCollectionUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_sample_collection_code(
    db: Session,
):

    count = get_sample_collection_count(
        db,
    )

    return f"SC{count + 1:06d}"


def create_sample_collection_service(
    db: Session,
    sample_collection: SampleCollectionCreate,
    current_user: User,
):

    lab_order = get_lab_order_by_id(
        db,
        sample_collection.lab_order_id,
    )

    if lab_order is None:

        not_found(
            "Lab Order not found."
        )

    if lab_order.status != "ORDERED":

        bad_request(
            "Sample has already been collected or processed."
        )

    new_sample = SampleCollection(

        sample_collection_code=generate_sample_collection_code(
            db,
        ),

        lab_order_id=sample_collection.lab_order_id,

        sample_type=sample_collection.sample_type,

        sample_container=sample_collection.sample_container,

        collected_by=sample_collection.collected_by,

        collection_datetime=sample_collection.collection_datetime,

        remarks=sample_collection.remarks,

        status="COLLECTED",
    )

    sample = create_sample_collection(
        db,
        new_sample,
    )

    lab_order.status = "COLLECTED"

    update_lab_order(
        db,
        lab_order,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="SAMPLE_COLLECTION",
        action="CREATE",
    )

    return sample


def get_all_sample_collections_service(
    db: Session,
    current_user: User,
):

    return get_all_sample_collections(
        db,
    )


def get_sample_collection_service(
    db: Session,
    sample_collection_id: int,
    current_user: User,
):

    sample = get_sample_collection_by_id(
        db,
        sample_collection_id,
    )

    if sample is None:

        not_found(
            "Sample Collection not found."
        )

    return sample


def update_sample_collection_service(
    db: Session,
    sample_collection_id: int,
    sample_collection_update: SampleCollectionUpdate,
    current_user: User,
):

    sample = get_sample_collection_by_id(
        db,
        sample_collection_id,
    )

    if sample is None:

        not_found(
            "Sample Collection not found."
        )

    update_data = sample_collection_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            sample,
            key,
            value,
        )

    updated = update_sample_collection(
        db,
        sample,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="SAMPLE_COLLECTION",
        action="UPDATE",
    )

    return updated


def delete_sample_collection_service(
    db: Session,
    sample_collection_id: int,
    current_user: User,
):

    sample = get_sample_collection_by_id(
        db,
        sample_collection_id,
    )

    if sample is None:

        not_found(
            "Sample Collection not found."
        )

    delete_sample_collection(
        db,
        sample,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="SAMPLE_COLLECTION",
        action="DELETE",
    )

    return {
        "message": "Sample Collection deleted successfully."
    }