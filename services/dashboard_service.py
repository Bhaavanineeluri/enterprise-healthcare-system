from sqlalchemy import func
from sqlalchemy.orm import Session

from models.appointment import Appointment
from models.billing import Billing
from models.doctor import Doctor
from models.insurance_claim import InsuranceClaim
from models.patient import Patient
from models.staff import Staff
from models.user import User


def get_dashboard_service(
    db: Session,
    current_user: User,
):

    return {

        "total_patients":
            db.query(Patient).count(),

        "total_doctors":
            db.query(Doctor).count(),

        "total_staff":
            db.query(Staff).count(),

        "total_appointments":
            db.query(Appointment).count(),

        "total_billings":
            db.query(Billing).count(),

        "total_revenue":
            db.query(
                func.coalesce(
                    func.sum(
                        Billing.net_amount,
                    ),
                    0,
                )
            ).scalar(),

        "total_insurance_claims":
            db.query(
                InsuranceClaim,
            ).count(),
    }