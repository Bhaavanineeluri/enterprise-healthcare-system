from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.payment_schema import (
    PaymentCreate,
    PaymentResponse,
    PaymentUpdate,
)

from services.payment_service import (
    create_payment_service,
    delete_payment_service,
    get_all_payments_service,
    get_payment_service,
    update_payment_service,
)


router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
)


@router.post(
    "/",
    response_model=PaymentResponse,
)
def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_payment_service(
        db=db,
        payment=payment,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[PaymentResponse],
)
def get_all_payments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_payments_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse,
)
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_payment_service(
        db=db,
        payment_id=payment_id,
        current_user=current_user,
    )


@router.put(
    "/{payment_id}",
    response_model=PaymentResponse,
)
def update_payment(
    payment_id: int,
    payment_update: PaymentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_payment_service(
        db=db,
        payment_id=payment_id,
        payment_update=payment_update,
        current_user=current_user,
    )


@router.delete(
    "/{payment_id}",
)
def delete_payment(
    payment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_payment_service(
        db=db,
        payment_id=payment_id,
        current_user=current_user,
    )