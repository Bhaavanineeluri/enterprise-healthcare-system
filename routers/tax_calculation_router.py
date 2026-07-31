from fastapi import APIRouter
from fastapi import Depends


from dependencies.auth import get_current_user
from models.user import User

from schemas.tax_calculation_schema import (
    TaxCalculationRequest,
    TaxCalculationResponse,
)

from services.tax_calculation_service import (
    calculate_tax_service,
)


router = APIRouter(
    prefix="/tax-calculation",
    tags=["Tax Calculation"],
)


@router.post(
    "/",
    response_model=TaxCalculationResponse,
)
def calculate_tax(
    tax: TaxCalculationRequest,
    current_user: User = Depends(get_current_user),
):

    return calculate_tax_service(
        tax=tax,
        current_user=current_user,
    )