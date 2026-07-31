from decimal import Decimal

from pydantic import BaseModel


class DashboardResponse(BaseModel):

    total_patients: int

    total_doctors: int

    total_staff: int

    total_appointments: int

    total_billings: int

    total_revenue: Decimal

    total_insurance_claims: int