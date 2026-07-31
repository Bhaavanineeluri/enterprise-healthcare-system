from sqlalchemy import func
from sqlalchemy.orm import Session

from models.billing import Billing
from models.payment import Payment
from models.refund import Refund
from models.user import User


def get_revenue_report_service(
    db: Session,
    current_user: User,
):

    total_billings = db.query(
        Billing
    ).count()

    total_revenue = (
        db.query(
            func.coalesce(
                func.sum(Billing.net_amount),
                0,
            )
        )
        .scalar()
    )

    total_payments = (
        db.query(
            func.coalesce(
                func.sum(Payment.amount_paid),
                0,
            )
        )
        .scalar()
    )

    total_refunds = (
        db.query(
            func.coalesce(
                func.sum(Refund.refund_amount),
                0,
            )
        )
        .scalar()
    )

    return {

        "total_billings": total_billings,

        "total_revenue": total_revenue,

        "total_payments": total_payments,

        "total_refunds": total_refunds,

        "net_revenue":
            total_payments - total_refunds,
    }