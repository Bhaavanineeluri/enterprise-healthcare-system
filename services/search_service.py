from sqlalchemy import or_
from sqlalchemy.orm import Session

from models.appointment import Appointment
from models.billing import Billing
from models.doctor import Doctor
from models.insurance_claim import InsuranceClaim
from models.invoice import Invoice
from models.patient import Patient
from models.staff import Staff
from models.user import User


def global_search_service(
    db: Session,
    query: str,
    current_user: User,
):

    results = []

    patients = (
        db.query(Patient)
        .filter(
            or_(
                Patient.first_name.ilike(f"%{query}%"),
                Patient.last_name.ilike(f"%{query}%"),
                Patient.patient_code.ilike(f"%{query}%"),
            )
        )
        .all()
    )

    for patient in patients:

        results.append({

            "module": "Patient",

            "id": patient.id,

            "title":
                f"{patient.patient_code} - {patient.first_name} {patient.last_name}",
        })

    doctors = (
        db.query(Doctor)
        .filter(
            Doctor.full_name.ilike(
                f"%{query}%"
            )
        )
        .all()
    )

    for doctor in doctors:

        results.append({

            "module": "Doctor",

            "id": doctor.id,

            "title":
                doctor.full_name,
        })

    staff = (
        db.query(Staff)
        .filter(
            Staff.full_name.ilike(
                f"%{query}%"
            )
        )
        .all()
    )

    for employee in staff:

        results.append({

            "module": "Staff",

            "id": employee.id,

            "title":
                employee.full_name,
        })

    bills = (
        db.query(Billing)
        .filter(
            Billing.bill_code.ilike(
                f"%{query}%"
            )
        )
        .all()
    )

    for bill in bills:

        results.append({

            "module": "Billing",

            "id": bill.id,

            "title":
                bill.bill_code,
        })

    invoices = (
        db.query(Invoice)
        .filter(
            Invoice.invoice_code.ilike(
                f"%{query}%"
            )
        )
        .all()
    )

    for invoice in invoices:

        results.append({

            "module": "Invoice",

            "id": invoice.id,

            "title":
                invoice.invoice_code,
        })

    claims = (
        db.query(
            InsuranceClaim
        )
        .filter(
            InsuranceClaim.claim_code.ilike(
                f"%{query}%"
            )
        )
        .all()
    )

    for claim in claims:

        results.append({

            "module":
                "Insurance Claim",

            "id":
                claim.id,

            "title":
                claim.claim_code,
        })

    appointments = (
        db.query(
            Appointment
        )
        .filter(
            Appointment.appointment_number.ilike(
                f"%{query}%"
            )
        )
        .all()
    )

    for appointment in appointments:

        results.append({

            "module":
                "Appointment",

            "id":
                appointment.id,

            "title":
                appointment.appointment_number,
        })

    return {

        "results": results
    }