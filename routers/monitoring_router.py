from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.monitoring_schema import (
    MonitoringResponse,
)

from services.monitoring_service import (
    get_monitoring_status_service,
)


router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring & Logging"],
)


@router.get(
    "/status",
    response_model=MonitoringResponse,
)
def monitoring_status(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_monitoring_status_service(
        db=db,
        current_user=current_user,
    )