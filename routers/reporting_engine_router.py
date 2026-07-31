from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.reporting_engine_schema import (
    ReportRequest,
    ReportResponse,
)

from services.reporting_engine_service import (
    generate_report_service,
)


router = APIRouter(
    prefix="/reporting-engine",
    tags=["Reporting Engine"],
)


@router.post(
    "/generate",
    response_model=ReportResponse,
)
def generate_report(
    report: ReportRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return generate_report_service(
        db=db,
        report=report,
        current_user=current_user,
    )