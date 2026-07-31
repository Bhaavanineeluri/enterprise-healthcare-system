from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.payment import Payment
from models.user import User

from repositories.billing_repository import (
    update_billing,
)

from repositories.invoice_repository import (
    get_invoice_by_id,
    update_invoice,
)

from repositories.payment_repository import (
    create_payment,
    delete_payment,
    get_all_payments,
    get_payment_by_id,
    get_payment_count,
    update_payment,
)

from schemas.payment_schema import (
    PaymentCreate,
    PaymentUpdate,
)

from services.audit_service import (
    save_audit_log,
)


VALID_PAYMENT_METHODS = {
    "CASH",
    "CARD",
    "UPI",
    "BANK_TRANSFER",
    "INSURANCE",
}

VALID_PAYMENT_STATUS = {
    "SUCCESS",
    "FAILED",
    "PENDING",
}


def generate_payment_code(
    db: Session,
):

    count = get_payment_count(db)

    return f"PAY{count + 1:06d}"


def create_payment_service(
    db: Session,
    payment: PaymentCreate,
    current_user: User,
):

    invoice = get_invoice_by_id(
        db,
        payment.invoice_id,
    )

    if invoice is None:

        not_found(
            "Invoice not found."
        )

    if payment.amount_paid <= 0:

        bad_request(
            "Payment amount must be greater than zero."
        )

    if payment.amount_paid != invoice.invoice_amount:

        bad_request(
            "Payment amount must match the invoice amount."
        )

    if payment.payment_method not in VALID_PAYMENT_METHODS:

        bad_request(
            "Invalid payment method."
        )

    new_payment = Payment(

        payment_code=generate_payment_code(
            db,
        ),

        invoice_id=payment.invoice_id,

        payment_date=payment.payment_date,

        amount_paid=payment.amount_paid,

        payment_method=payment.payment_method,

        payment_status="SUCCESS",

        transaction_reference=payment.transaction_reference,

        remarks=payment.remarks,
    )

    created = create_payment(
        db,
        new_payment,
    )

    invoice.invoice_status = "PAID"

    update_invoice(
        db,
        invoice,
    )

    billing = invoice.billing

    billing.payment_status = "PAID"

    update_billing(
        db,
        billing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PAYMENT",
        action="CREATE",
    )

    return created


def get_all_payments_service(
    db: Session,
    current_user: User,
):

    return get_all_payments(
        db,
    )


def get_payment_service(
    db: Session,
    payment_id: int,
    current_user: User,
):

    payment = get_payment_by_id(
        db,
        payment_id,
    )

    if payment is None:

        not_found(
            "Payment not found."
        )

    return payment


def update_payment_service(
    db: Session,
    payment_id: int,
    payment_update: PaymentUpdate,
    current_user: User,
):

    payment = get_payment_by_id(
        db,
        payment_id,
    )

    if payment is None:

        not_found(
            "Payment not found."
        )

    update_data = payment_update.model_dump(
        exclude_unset=True,
    )

    if (
        "payment_method" in update_data
        and update_data["payment_method"] not in VALID_PAYMENT_METHODS
    ):

        bad_request(
            "Invalid payment method."
        )

    if (
        "payment_status" in update_data
        and update_data["payment_status"] not in VALID_PAYMENT_STATUS
    ):

        bad_request(
            "Invalid payment status."
        )

    for key, value in update_data.items():

        setattr(
            payment,
            key,
            value,
        )

    updated = update_payment(
        db,
        payment,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PAYMENT",
        action="UPDATE",
    )

    return updated


def delete_payment_service(
    db: Session,
    payment_id: int,
    current_user: User,
):

    payment = get_payment_by_id(
        db,
        payment_id,
    )

    if payment is None:

        not_found(
            "Payment not found."
        )

    delete_payment(
        db,
        payment,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="PAYMENT",
        action="DELETE",
    )

    return {
        "message": "Payment deleted successfully."
    }