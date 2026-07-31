from sqlalchemy import func
from sqlalchemy.orm import Session

from models.insurance_claim import InsuranceClaim
from models.invoice import Invoice
from models.payment import Payment
from models.refund import Refund
from models.user import User


def get_financial_report_service(
    db: Session,
    current_user: User,
):

    total_invoices = db.query(
        Invoice
    ).count()

    total_invoice_amount = (
        db.query(
            func.coalesce(
                func.sum(
                    Invoice.invoice_amount,
                ),
                0,
            )
        )
        .scalar()
    )

    total_payments = db.query(
        Payment
    ).count()

    total_payment_amount = (
        db.query(
            func.coalesce(
                func.sum(
                    Payment.amount_paid,
                ),
                0,
            )
        )
        .scalar()
    )

    total_refunds = db.query(
        Refund
    ).count()

    total_refund_amount = (
        db.query(
            func.coalesce(
                func.sum(
                    Refund.refund_amount,
                ),
                0,
            )
        )
        .scalar()
    )

    total_insurance_claims = db.query(
        InsuranceClaim
    ).count()

    total_claim_amount = (
        db.query(
            func.coalesce(
                func.sum(
                    InsuranceClaim.claim_amount,
                ),
                0,
            )
        )
        .scalar()
    )

    return {

        "total_invoices": total_invoices,

        "total_invoice_amount": total_invoice_amount,

        "total_payments": total_payments,

        "total_payment_amount": total_payment_amount,

        "total_refunds": total_refunds,

        "total_refund_amount": total_refund_amount,

        "total_insurance_claims": total_insurance_claims,

        "total_claim_amount": total_claim_amount,
    }