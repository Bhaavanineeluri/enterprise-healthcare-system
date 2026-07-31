from decimal import Decimal

from pydantic import BaseModel


class FinancialReportResponse(BaseModel):

    total_invoices: int

    total_invoice_amount: Decimal

    total_payments: int

    total_payment_amount: Decimal

    total_refunds: int

    total_refund_amount: Decimal

    total_insurance_claims: int

    total_claim_amount: Decimal