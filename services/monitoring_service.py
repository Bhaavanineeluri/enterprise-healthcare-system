from sqlalchemy import text
from sqlalchemy.orm import Session

from config.settings import settings

from models.user import User


def get_monitoring_status_service(
    db: Session,
    current_user: User,
):

    database_status = "Connected"

    try:

        db.execute(
            text("SELECT 1")
        )

    except Exception:

        database_status = "Disconnected"

    return {

        "application": settings.APP_NAME,

        "status": "Running",

        "database": database_status,

        "logging": "Enabled",
    }