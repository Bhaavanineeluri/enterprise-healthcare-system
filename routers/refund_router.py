from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.refund_schema import (
    RefundCreate,
    RefundResponse,
    RefundUpdate,
)

from services.refund_service import (
    create_refund_service,
    delete_refund_service,
    get_all_refunds_service,
    get_refund_service,
    update_refund_service,
)


router = APIRouter(
    prefix="/refunds",
    tags=["Refunds"],
)


@router.post(
    "/",
    response_model=RefundResponse,
)
def create_refund(
    refund: RefundCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_refund_service(
        db=db,
        refund=refund,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[RefundResponse],
)
def get_all_refunds(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_refunds_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{refund_id}",
    response_model=RefundResponse,
)
def get_refund(
    refund_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_refund_service(
        db=db,
        refund_id=refund_id,
        current_user=current_user,
    )


@router.put(
    "/{refund_id}",
    response_model=RefundResponse,
)
def update_refund(
    refund_id: int,
    refund_update: RefundUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_refund_service(
        db=db,
        refund_id=refund_id,
        refund_update=refund_update,
        current_user=current_user,
    )


@router.delete(
    "/{refund_id}",
)
def delete_refund(
    refund_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_refund_service(
        db=db,
        refund_id=refund_id,
        current_user=current_user,
    )