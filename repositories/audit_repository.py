from sqlalchemy.orm import Session

from models.audit_log import AuditLog


def create_audit_log(
    db: Session,
    audit: AuditLog
):

    db.add(audit)
    db.commit()
    db.refresh(audit)

    return audit


def get_all_audit_logs(
    db: Session
):

    return db.query(AuditLog).all()


def get_user_audit_logs(
    db: Session,
    user_id: int
):

    return (
        db.query(AuditLog)
        .filter(AuditLog.user_id == user_id)
        .all()
    )