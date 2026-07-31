from sqlalchemy.orm import Session

from models.audit_log import AuditLog
from models.user import User


def get_all_audit_reports_service(
    db: Session,
    current_user: User,
):

    return (
        db.query(AuditLog)
        .order_by(
            AuditLog.created_at.desc()
        )
        .all()
    )


def get_audit_report_service(
    db: Session,
    audit_id: int,
    current_user: User,
):

    return (
        db.query(AuditLog)
        .filter(
            AuditLog.id == audit_id
        )
        .first()
    )


def get_audit_reports_by_module_service(
    db: Session,
    module: str,
    current_user: User,
):

    return (
        db.query(AuditLog)
        .filter(
            AuditLog.module == module
        )
        .order_by(
            AuditLog.created_at.desc()
        )
        .all()
    )


def get_audit_reports_by_action_service(
    db: Session,
    action: str,
    current_user: User,
):

    return (
        db.query(AuditLog)
        .filter(
            AuditLog.action == action
        )
        .order_by(
            AuditLog.created_at.desc()
        )
        .all()
    )


def get_audit_reports_by_user_service(
    db: Session,
    user_id: int,
    current_user: User,
):

    return (
        db.query(AuditLog)
        .filter(
            AuditLog.user_id == user_id
        )
        .order_by(
            AuditLog.created_at.desc()
        )
        .all()
    )