from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.billing_schema import (
    BillingCreate,
    BillingResponse,
    BillingUpdate,
)

from services.billing_service import (
    create_billing_service,
    delete_billing_service,
    get_all_billings_service,
    get_billing_service,
    update_billing_service,
)


router = APIRouter(
    prefix="/billings",
    tags=["Billing"],
)


@router.post(
    "/",
    response_model=BillingResponse,
)
def create_billing(
    billing: BillingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_billing_service(
        db=db,
        billing=billing,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[BillingResponse],
)
def get_all_billings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_billings_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{billing_id}",
    response_model=BillingResponse,
)
def get_billing(
    billing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_billing_service(
        db=db,
        billing_id=billing_id,
        current_user=current_user,
    )


@router.put(
    "/{billing_id}",
    response_model=BillingResponse,
)
def update_billing(
    billing_id: int,
    billing_update: BillingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_billing_service(
        db=db,
        billing_id=billing_id,
        billing_update=billing_update,
        current_user=current_user,
    )


@router.delete(
    "/{billing_id}",
)
def delete_billing(
    billing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_billing_service(
        db=db,
        billing_id=billing_id,
        current_user=current_user,
    )