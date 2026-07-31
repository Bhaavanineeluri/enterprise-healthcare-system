from decimal import Decimal

from pydantic import BaseModel


class TaxCalculationRequest(BaseModel):

    amount: Decimal

    tax_percentage: Decimal


class TaxCalculationResponse(BaseModel):

    amount: Decimal

    tax_percentage: Decimal

    tax_amount: Decimal

    total_amount: Decimal