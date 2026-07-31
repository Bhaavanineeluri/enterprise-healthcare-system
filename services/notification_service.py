from models.user import User

from schemas.notification_schema import (
    NotificationRequest,
)


def send_notification_service(
    notification: NotificationRequest,
    current_user: User,
):

    """
    Future implementations:

    - Email
    - SMS
    - Push Notification
    - WhatsApp
    """

    return {

        "success": True,

        "message":
            "Notification sent successfully."
    }