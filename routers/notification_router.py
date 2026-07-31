from fastapi import APIRouter
from fastapi import Depends


from dependencies.auth import get_current_user
from models.user import User

from schemas.notification_schema import (
    NotificationRequest,
    NotificationResponse,
)

from services.notification_service import (
    send_notification_service,
)


router = APIRouter(
    prefix="/notifications",
    tags=["Notification Service"],
)


@router.post(
    "/send",
    response_model=NotificationResponse,
)
def send_notification(
    notification: NotificationRequest,
    current_user: User = Depends(get_current_user),
):

    return send_notification_service(
        notification=notification,
        current_user=current_user,
    )