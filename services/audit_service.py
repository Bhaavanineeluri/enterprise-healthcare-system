from sqlalchemy.orm import Session

from models.audit_log import AuditLog
from models.user import User
from repositories.audit_repository import create_audit_log


def save_audit_log(
    db: Session,
    current_user: User,
    module: str,
    action: str,
):

    audit = AuditLog(
        user_id=current_user.id,
        username=current_user.username,
        role=current_user.role.role_name,
        module=module,
        action=action,
    )

    return create_audit_log(
        db,
        audit,
    )