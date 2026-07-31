from decimal import Decimal

from models.user import User

from schemas.tax_calculation_schema import (
    TaxCalculationRequest,
)


def calculate_tax_service(
    tax: TaxCalculationRequest,
    current_user: User,
):

    tax_amount = (
        tax.amount * tax.tax_percentage
    ) / Decimal("100")

    total_amount = (
        tax.amount + tax_amount
    )

    return {

        "amount": tax.amount,

        "tax_percentage": tax.tax_percentage,

        "tax_amount": tax_amount,

        "total_amount": total_amount,
    }