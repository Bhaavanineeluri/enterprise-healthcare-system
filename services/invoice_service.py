from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.invoice import Invoice
from models.user import User

from repositories.billing_repository import (
    get_billing_by_id,
)

from repositories.invoice_repository import (
    create_invoice,
    delete_invoice,
    get_all_invoices,
    get_invoice_by_id,
    get_invoice_count,
    update_invoice,
)

from schemas.invoice_schema import (
    InvoiceCreate,
    InvoiceUpdate,
)

from services.audit_service import (
    save_audit_log,
)


VALID_INVOICE_STATUS = {
    "UNPAID",
    "PARTIALLY_PAID",
    "PAID",
    "CANCELLED",
}


def generate_invoice_code(
    db: Session,
):

    count = get_invoice_count(db)

    return f"INV{count + 1:06d}"


def create_invoice_service(
    db: Session,
    invoice: InvoiceCreate,
    current_user: User,
):

    billing = get_billing_by_id(
        db,
        invoice.billing_id,
    )

    if billing is None:

        not_found(
            "Billing record not found."
        )

    if invoice.due_date < invoice.invoice_date:

        bad_request(
            "Due date cannot be before invoice date."
        )

    new_invoice = Invoice(

        invoice_code=generate_invoice_code(
            db,
        ),

        billing_id=invoice.billing_id,

        invoice_date=invoice.invoice_date,

        due_date=invoice.due_date,

        invoice_amount=billing.net_amount,

        invoice_status="UNPAID",

        remarks=invoice.remarks,
    )

    created = create_invoice(
        db,
        new_invoice,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="INVOICE",
        action="CREATE",
    )

    return created


def get_all_invoices_service(
    db: Session,
    current_user: User,
):

    return get_all_invoices(
        db,
    )


def get_invoice_service(
    db: Session,
    invoice_id: int,
    current_user: User,
):

    invoice = get_invoice_by_id(
        db,
        invoice_id,
    )

    if invoice is None:

        not_found(
            "Invoice not found."
        )

    return invoice


def update_invoice_service(
    db: Session,
    invoice_id: int,
    invoice_update: InvoiceUpdate,
    current_user: User,
):

    invoice = get_invoice_by_id(
        db,
        invoice_id,
    )

    if invoice is None:

        not_found(
            "Invoice not found."
        )

    update_data = invoice_update.model_dump(
        exclude_unset=True,
    )

    if (
        "invoice_status" in update_data
        and update_data["invoice_status"] not in VALID_INVOICE_STATUS
    ):

        bad_request(
            "Invalid invoice status."
        )

    if (
        "due_date" in update_data
        and update_data["due_date"] < invoice.invoice_date
    ):

        bad_request(
            "Due date cannot be before invoice date."
        )

    for key, value in update_data.items():

        setattr(
            invoice,
            key,
            value,
        )

    updated = update_invoice(
        db,
        invoice,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="INVOICE",
        action="UPDATE",
    )

    return updated


def delete_invoice_service(
    db: Session,
    invoice_id: int,
    current_user: User,
):

    invoice = get_invoice_by_id(
        db,
        invoice_id,
    )

    if invoice is None:

        not_found(
            "Invoice not found."
        )

    delete_invoice(
        db,
        invoice,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="INVOICE",
        action="DELETE",
    )

    return {
        "message": "Invoice deleted successfully."
    }