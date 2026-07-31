from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.pharmacy_inventory_schema import (
    PharmacyInventoryCreate,
    PharmacyInventoryResponse,
    PharmacyInventoryUpdate,
)

from services.pharmacy_inventory_service import (
    create_pharmacy_inventory_service,
    delete_pharmacy_inventory_service,
    get_all_pharmacy_inventory_service,
    get_pharmacy_inventory_service,
    update_pharmacy_inventory_service,
)


router = APIRouter(
    prefix="/pharmacy-inventory",
    tags=["Pharmacy Inventory"],
)


@router.post(
    "/",
    response_model=PharmacyInventoryResponse,
)
def create_inventory(
    inventory: PharmacyInventoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_pharmacy_inventory_service(
        db=db,
        inventory=inventory,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[PharmacyInventoryResponse],
)
def get_all_inventory(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    
):

    return get_all_pharmacy_inventory_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{inventory_id}",
    response_model=PharmacyInventoryResponse,
)
def get_inventory(
    inventory_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_pharmacy_inventory_service(
        db=db,
        inventory_id=inventory_id,
        current_user=current_user,
    )


@router.put(
    "/{inventory_id}",
    response_model=PharmacyInventoryResponse,
)
def update_inventory(
    inventory_id: int,
    inventory_update: PharmacyInventoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_pharmacy_inventory_service(
        db=db,
        inventory_id=inventory_id,
        inventory_update=inventory_update,
        current_user=current_user,
    )


@router.delete(
    "/{inventory_id}",
)
def delete_inventory(
    inventory_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_pharmacy_inventory_service(
        db=db,
        inventory_id=inventory_id,
        current_user=current_user,
    )