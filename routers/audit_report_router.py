from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.audit_report_schema import (
    AuditReportResponse,
)

from services.audit_report_service import (
    get_all_audit_reports_service,
    get_audit_report_service,
    get_audit_reports_by_action_service,
    get_audit_reports_by_module_service,
    get_audit_reports_by_user_service,
)


router = APIRouter(
    prefix="/audit-reports",
    tags=["Audit Reports"],
)


@router.get(
    "/",
    response_model=list[AuditReportResponse],
)
def get_all_audit_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_audit_reports_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{audit_id}",
    response_model=AuditReportResponse,
)
def get_audit_report(
    audit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_audit_report_service(
        db=db,
        audit_id=audit_id,
        current_user=current_user,
    )


@router.get(
    "/module/{module}",
    response_model=list[AuditReportResponse],
)
def get_by_module(
    module: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_audit_reports_by_module_service(
        db=db,
        module=module,
        current_user=current_user,
    )


@router.get(
    "/action/{action}",
    response_model=list[AuditReportResponse],
)
def get_by_action(
    action: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_audit_reports_by_action_service(
        db=db,
        action=action,
        current_user=current_user,
    )


@router.get(
    "/user/{user_id}",
    response_model=list[AuditReportResponse],
)
def get_by_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_audit_reports_by_user_service(
        db=db,
        user_id=user_id,
        current_user=current_user,
    )