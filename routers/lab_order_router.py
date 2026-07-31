from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.lab_order_schema import (
    LabOrderCreate,
    LabOrderResponse,
    LabOrderUpdate,
)

from services.lab_order_service import (
    create_lab_order_service,
    delete_lab_order_service,
    get_all_lab_orders_service,
    get_lab_order_service,
    update_lab_order_service,
)


router = APIRouter(
    prefix="/lab-orders",
    tags=["Lab Orders"],
)


@router.post(
    "/",
    response_model=LabOrderResponse,
)
def create_lab_order(
    lab_order: LabOrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_lab_order_service(
        db=db,
        lab_order=lab_order,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[LabOrderResponse],
)
def get_all_lab_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_lab_orders_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{lab_order_id}",
    response_model=LabOrderResponse,
)
def get_lab_order(
    lab_order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_lab_order_service(
        db=db,
        lab_order_id=lab_order_id,
        current_user=current_user,
    )


@router.put(
    "/{lab_order_id}",
    response_model=LabOrderResponse,
)
def update_lab_order(
    lab_order_id: int,
    lab_order_update: LabOrderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_lab_order_service(
        db=db,
        lab_order_id=lab_order_id,
        lab_order_update=lab_order_update,
        current_user=current_user,
    )


@router.delete(
    "/{lab_order_id}",
)
def delete_lab_order(
    lab_order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_lab_order_service(
        db=db,
        lab_order_id=lab_order_id,
        current_user=current_user,
    )