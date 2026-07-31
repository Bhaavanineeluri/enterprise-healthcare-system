from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.refund import Refund
from models.user import User

from repositories.payment_repository import (
    get_payment_by_id,
    update_payment,
)

from repositories.refund_repository import (
    create_refund,
    delete_refund,
    get_all_refunds,
    get_refund_by_id,
    get_refund_count,
    update_refund,
)

from schemas.refund_schema import (
    RefundCreate,
    RefundUpdate,
)

from services.audit_service import (
    save_audit_log,
)


VALID_REFUND_STATUS = {
    "PENDING",
    "COMPLETED",
    "REJECTED",
}


def generate_refund_code(
    db: Session,
):

    count = get_refund_count(db)

    return f"REF{count + 1:06d}"


def create_refund_service(
    db: Session,
    refund: RefundCreate,
    current_user: User,
):

    payment = get_payment_by_id(
        db,
        refund.payment_id,
    )

    if payment is None:

        not_found(
            "Payment not found."
        )

    if refund.refund_amount <= 0:

        bad_request(
            "Refund amount must be greater than zero."
        )

    if refund.refund_amount > payment.amount_paid:

        bad_request(
            "Refund amount cannot exceed the payment amount."
        )

    new_refund = Refund(

        refund_code=generate_refund_code(
            db,
        ),

        payment_id=refund.payment_id,

        refund_amount=refund.refund_amount,

        refund_date=refund.refund_date,

        refund_reason=refund.refund_reason,

        refund_status="COMPLETED",

        remarks=refund.remarks,
    )

    created = create_refund(
        db,
        new_refund,
    )

    payment.payment_status = "REFUNDED"

    update_payment(
        db,
        payment,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="REFUND",
        action="CREATE",
    )

    return created


def get_all_refunds_service(
    db: Session,
    current_user: User,
):

    return get_all_refunds(
        db,
    )


def get_refund_service(
    db: Session,
    refund_id: int,
    current_user: User,
):

    refund = get_refund_by_id(
        db,
        refund_id,
    )

    if refund is None:

        not_found(
            "Refund not found."
        )

    return refund


def update_refund_service(
    db: Session,
    refund_id: int,
    refund_update: RefundUpdate,
    current_user: User,
):

    refund = get_refund_by_id(
        db,
        refund_id,
    )

    if refund is None:

        not_found(
            "Refund not found."
        )

    update_data = refund_update.model_dump(
        exclude_unset=True,
    )

    if (
        "refund_status" in update_data
        and update_data["refund_status"] not in VALID_REFUND_STATUS
    ):

        bad_request(
            "Invalid refund status."
        )

    for key, value in update_data.items():

        setattr(
            refund,
            key,
            value,
        )

    updated = update_refund(
        db,
        refund,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="REFUND",
        action="UPDATE",
    )

    return updated


def delete_refund_service(
    db: Session,
    refund_id: int,
    current_user: User,
):

    refund = get_refund_by_id(
        db,
        refund_id,
    )

    if refund is None:

        not_found(
            "Refund not found."
        )

    delete_refund(
        db,
        refund,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="REFUND",
        action="DELETE",
    )

    return {
        "message": "Refund deleted successfully."
    }