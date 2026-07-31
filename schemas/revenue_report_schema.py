from decimal import Decimal

from pydantic import BaseModel


class RevenueReportResponse(BaseModel):

    total_billings: int

    total_revenue: Decimal

    total_payments: Decimal

    total_refunds: Decimal

    net_revenue: Decimal