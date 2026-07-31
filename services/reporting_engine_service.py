from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
)

from models.appointment import Appointment
from models.billing import Billing
from models.insurance_claim import InsuranceClaim
from models.lab_order import LabOrder
from models.patient import Patient
from models.pharmacy_inventory import PharmacyInventory
from models.user import User

from schemas.reporting_engine_schema import (
    ReportRequest,
)


def generate_report_service(
    db: Session,
    report: ReportRequest,
    current_user: User,
):

    report_mapping = {

        "PATIENT": Patient,

        "APPOINTMENT": Appointment,

        "BILLING": Billing,

        "LABORATORY": LabOrder,

        "PHARMACY": PharmacyInventory,

        "INSURANCE": InsuranceClaim,
    }

    model = report_mapping.get(
        report.report_type,
    )

    if model is None:

        bad_request(
            "Invalid report type.",
        )

    total_records = (
        db.query(model)
        .count()
    )

    return {

        "report_type":
            report.report_type,

        "total_records":
            total_records,

        "message":
            f"{report.report_type} report generated successfully.",
    }