from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.expiry_management_schema import (
    ExpiryManagementCreate,
    ExpiryManagementResponse,
    ExpiryManagementUpdate,
)

from services.expiry_management_service import (
    create_expiry_management_service,
    delete_expiry_management_service,
    get_all_expiry_management_service,
    get_expiry_management_service,
    update_expiry_management_service,
)


router = APIRouter(
    prefix="/expiry-management",
    tags=["Expiry Management"],
)


@router.post(
    "/",
    response_model=ExpiryManagementResponse,
)
def create_expiry_management(
    expiry: ExpiryManagementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_expiry_management_service(
        db=db,
        expiry=expiry,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[ExpiryManagementResponse],
)
def get_all_expiry_management(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_expiry_management_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{expiry_id}",
    response_model=ExpiryManagementResponse,
)
def get_expiry_management(
    expiry_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_expiry_management_service(
        db=db,
        expiry_id=expiry_id,
        current_user=current_user,
    )


@router.put(
    "/{expiry_id}",
    response_model=ExpiryManagementResponse,
)
def update_expiry_management(
    expiry_id: int,
    expiry_update: ExpiryManagementUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_expiry_management_service(
        db=db,
        expiry_id=expiry_id,
        expiry_update=expiry_update,
        current_user=current_user,
    )


@router.delete(
    "/{expiry_id}",
)
def delete_expiry_management(
    expiry_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_expiry_management_service(
        db=db,
        expiry_id=expiry_id,
        current_user=current_user,
    )