from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.financial_report_schema import (
    FinancialReportResponse,
)

from services.financial_report_service import (
    get_financial_report_service,
)


router = APIRouter(
    prefix="/financial-reports",
    tags=["Financial Reports"],
)


@router.get(
    "/",
    response_model=FinancialReportResponse,
)
def get_financial_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_financial_report_service(
        db=db,
        current_user=current_user,
    )