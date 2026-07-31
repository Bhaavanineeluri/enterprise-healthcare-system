from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.dashboard_schema import (
    DashboardResponse,
)

from services.dashboard_service import (
    get_dashboard_service,
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard & Analytics"],
)


@router.get(
    "/",
    response_model=DashboardResponse,
)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_dashboard_service(
        db=db,
        current_user=current_user,
    )