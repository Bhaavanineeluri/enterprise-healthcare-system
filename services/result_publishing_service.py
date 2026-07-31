from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.result_publishing import ResultPublishing
from models.user import User

from repositories.lab_order_repository import (
    get_lab_order_by_id,
    update_lab_order,
)

from repositories.result_publishing_repository import (
    create_result,
    delete_result,
    get_all_results,
    get_result_by_id,
    get_result_count,
    update_result,
)

from schemas.result_publishing_schema import (
    ResultPublishingCreate,
    ResultPublishingUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_result_code(
    db: Session,
):

    return f"RPT{get_result_count(db)+1:06d}"


def create_result_service(
    db: Session,
    result: ResultPublishingCreate,
    current_user: User,
):

    lab_order = get_lab_order_by_id(
        db,
        result.lab_order_id,
    )

    if lab_order is None:

        not_found(
            "Lab Order not found."
        )

    if lab_order.status != "PROCESSING":

        bad_request(
            "Test processing must be completed first."
        )

    new_result = ResultPublishing(

        result_code=generate_result_code(db),

        lab_order_id=result.lab_order_id,

        result=result.result,

        reference_range=result.reference_range,

        interpretation=result.interpretation,

        approved_by=result.approved_by,

        published_at=result.published_at,

        status="COMPLETED",
    )

    created = create_result(
        db,
        new_result,
    )

    lab_order.status = "COMPLETED"

    update_lab_order(
        db,
        lab_order,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="RESULT_PUBLISHING",
        action="CREATE",
    )

    return created


def get_all_results_service(
    db: Session,
):
    return get_all_results(db)


def get_result_service(
    db: Session,
    result_id: int,
):

    result = get_result_by_id(
        db,
        result_id,
    )

    if result is None:

        not_found(
            "Result not found."
        )

    return result


def update_result_service(
    db: Session,
    result_id: int,
    result_update: ResultPublishingUpdate,
    current_user: User,
):

    result = get_result_by_id(
        db,
        result_id,
    )

    if result is None:

        not_found(
            "Result not found."
        )

    update_data = result_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            result,
            key,
            value,
        )

    updated = update_result(
        db,
        result,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="RESULT_PUBLISHING",
        action="UPDATE",
    )

    return updated


def delete_result_service(
    db: Session,
    result_id: int,
    current_user: User,
):

    result = get_result_by_id(
        db,
        result_id,
    )

    if result is None:

        not_found(
            "Result not found."
        )

    delete_result(
        db,
        result,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="RESULT_PUBLISHING",
        action="DELETE",
    )

    return {
        "message": "Result deleted successfully."
    }