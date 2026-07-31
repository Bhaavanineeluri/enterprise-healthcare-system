from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.test_processing import TestProcessing
from models.user import User

from repositories.test_processing_repository import (
    create_test_processing,
    delete_test_processing,
    get_all_test_processing,
    get_test_processing_by_id,
    get_test_processing_count,
    update_test_processing,
)

from repositories.lab_order_repository import (
    get_lab_order_by_id,
    update_lab_order,
)

from schemas.test_processing_schema import (
    TestProcessingCreate,
    TestProcessingUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_processing_code(
    db: Session,
):

    count = get_test_processing_count(
        db,
    )

    return f"TP{count + 1:06d}"


def create_test_processing_service(
    db: Session,
    processing: TestProcessingCreate,
    current_user: User,
):

    lab_order = get_lab_order_by_id(
        db,
        processing.lab_order_id,
    )

    if lab_order is None:

        not_found(
            "Lab Order not found."
        )

    if lab_order.status != "COLLECTED":

        bad_request(
            "Sample must be collected before processing."
        )

    new_processing = TestProcessing(

        processing_code=generate_processing_code(
            db,
        ),

        lab_order_id=processing.lab_order_id,

        processed_by=processing.processed_by,

        processing_start=processing.processing_start,

        processing_end=processing.processing_end,

        observations=processing.observations,

        remarks=processing.remarks,

        status="PROCESSING",
    )

    processing_data = create_test_processing(
        db,
        new_processing,
    )

    lab_order.status = "PROCESSING"

    update_lab_order(
        db,
        lab_order,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="TEST_PROCESSING",
        action="CREATE",
    )

    return processing_data


def get_all_test_processing_service(
    db: Session,
    current_user: User,
):

    return get_all_test_processing(
        db,
    )


def get_test_processing_service(
    db: Session,
    processing_id: int,
    current_user: User,
):

    processing = get_test_processing_by_id(
        db,
        processing_id,
    )

    if processing is None:

        not_found(
            "Test Processing record not found."
        )

    return processing


def update_test_processing_service(
    db: Session,
    processing_id: int,
    processing_update: TestProcessingUpdate,
    current_user: User,
):

    processing = get_test_processing_by_id(
        db,
        processing_id,
    )

    if processing is None:

        not_found(
            "Test Processing record not found."
        )

    update_data = processing_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            processing,
            key,
            value,
        )

    updated = update_test_processing(
        db,
        processing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="TEST_PROCESSING",
        action="UPDATE",
    )

    return updated


def delete_test_processing_service(
    db: Session,
    processing_id: int,
    current_user: User,
):

    processing = get_test_processing_by_id(
        db,
        processing_id,
    )

    if processing is None:

        not_found(
            "Test Processing record not found."
        )

    delete_test_processing(
        db,
        processing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="TEST_PROCESSING",
        action="DELETE",
    )

    return {
        "message": "Test Processing deleted successfully."
    }