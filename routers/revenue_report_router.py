from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.revenue_report_schema import (
    RevenueReportResponse,
)

from services.revenue_report_service import (
    get_revenue_report_service,
)


router = APIRouter(
    prefix="/revenue-reports",
    tags=["Revenue Reports"],
)


@router.get(
    "/",
    response_model=RevenueReportResponse,
)
def get_revenue_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_revenue_report_service(
        db=db,
        current_user=current_user,
    )