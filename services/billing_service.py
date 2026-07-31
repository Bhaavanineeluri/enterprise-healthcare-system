from decimal import Decimal

from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.billing import Billing
from models.user import User

from repositories.appointment_repository import (
    get_appointment_by_id,
)

from repositories.billing_repository import (
    create_billing,
    delete_billing,
    get_all_billings,
    get_billing_by_id,
    get_billing_count,
    update_billing,
)

from repositories.patient_repository import (
    get_patient_by_id,
)

from schemas.billing_schema import (
    BillingCreate,
    BillingUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_billing_code(
    db: Session,
):

    count = get_billing_count(db)

    return f"BILL{count + 1:06d}"


def calculate_net_amount(
    total_amount: Decimal,
    discount: Decimal,
    tax: Decimal,
):

    return total_amount - discount + tax


def create_billing_service(
    db: Session,
    billing: BillingCreate,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        billing.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    appointment = get_appointment_by_id(
        db,
        billing.appointment_id,
    )

    if appointment is None:

        not_found(
            "Appointment not found."
        )

    if billing.total_amount < 0:

        bad_request(
            "Total amount cannot be negative."
        )

    if billing.discount < 0:

        bad_request(
            "Discount cannot be negative."
        )

    if billing.tax < 0:

        bad_request(
            "Tax cannot be negative."
        )

    if billing.discount > billing.total_amount:

        bad_request(
            "Discount cannot exceed total amount."
        )

    net_amount = calculate_net_amount(
        billing.total_amount,
        billing.discount,
        billing.tax,
    )

    new_billing = Billing(

        billing_code=generate_billing_code(
            db,
        ),

        patient_id=billing.patient_id,

        appointment_id=billing.appointment_id,

        total_amount=billing.total_amount,

        discount=billing.discount,

        tax=billing.tax,

        net_amount=net_amount,

        billing_date=billing.billing_date,

        payment_status="PENDING",

        remarks=billing.remarks,
    )

    created = create_billing(
        db,
        new_billing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BILLING",
        action="CREATE",
    )

    return created


def get_all_billings_service(
    db: Session,
    current_user: User,
):

    return get_all_billings(db)


def get_billing_service(
    db: Session,
    billing_id: int,
    current_user: User,
):

    billing = get_billing_by_id(
        db,
        billing_id,
    )

    if billing is None:

        not_found(
            "Billing record not found."
        )

    return billing


def update_billing_service(
    db: Session,
    billing_id: int,
    billing_update: BillingUpdate,
    current_user: User,
):

    billing = get_billing_by_id(
        db,
        billing_id,
    )

    if billing is None:

        not_found(
            "Billing record not found."
        )

    update_data = billing_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            billing,
            key,
            value,
        )

    if (
        "total_amount" in update_data
        or "discount" in update_data
        or "tax" in update_data
    ):

        billing.net_amount = calculate_net_amount(
            billing.total_amount,
            billing.discount,
            billing.tax,
        )

    updated = update_billing(
        db,
        billing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BILLING",
        action="UPDATE",
    )

    return updated


def delete_billing_service(
    db: Session,
    billing_id: int,
    current_user: User,
):

    billing = get_billing_by_id(
        db,
        billing_id,
    )

    if billing is None:

        not_found(
            "Billing record not found."
        )

    delete_billing(
        db,
        billing,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BILLING",
        action="DELETE",
    )

    return {
        "message": "Billing deleted successfully."
    }