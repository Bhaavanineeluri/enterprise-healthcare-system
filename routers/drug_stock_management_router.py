from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.drug_stock_management_schema import (
    DrugStockManagementCreate,
    DrugStockManagementResponse,
    DrugStockManagementUpdate,
)

from services.drug_stock_management_service import (
    create_drug_stock_management_service,
    delete_drug_stock_management_service,
    get_all_drug_stock_management_service,
    get_drug_stock_management_service,
    update_drug_stock_management_service,
)


router = APIRouter(
    prefix="/drug-stock-management",
    tags=["Drug Stock Management"],
)


@router.post(
    "/",
    response_model=DrugStockManagementResponse,
)
def create_drug_stock_management(
    stock: DrugStockManagementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_drug_stock_management_service(
        db=db,
        stock=stock,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[DrugStockManagementResponse],
)
def get_all_drug_stock_management(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_drug_stock_management_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{stock_id}",
    response_model=DrugStockManagementResponse,
)
def get_drug_stock_management(
    stock_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_drug_stock_management_service(
        db=db,
        stock_id=stock_id,
        current_user=current_user,
    )


@router.put(
    "/{stock_id}",
    response_model=DrugStockManagementResponse,
)
def update_drug_stock_management(
    stock_id: int,
    stock_update: DrugStockManagementUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_drug_stock_management_service(
        db=db,
        stock_id=stock_id,
        stock_update=stock_update,
        current_user=current_user,
    )


@router.delete(
    "/{stock_id}",
)
def delete_drug_stock_management(
    stock_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_drug_stock_management_service(
        db=db,
        stock_id=stock_id,
        current_user=current_user,
    )