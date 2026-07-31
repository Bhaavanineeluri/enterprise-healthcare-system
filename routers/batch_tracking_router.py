from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.batch_tracking_schema import (
    BatchTrackingCreate,
    BatchTrackingResponse,
    BatchTrackingUpdate,
)

from services.batch_tracking_service import (
    create_batch_tracking_service,
    delete_batch_tracking_service,
    get_all_batch_tracking_service,
    get_batch_tracking_service,
    update_batch_tracking_service,
)


router = APIRouter(
    prefix="/batch-tracking",
    tags=["Batch Tracking"],
)


@router.post(
    "/",
    response_model=BatchTrackingResponse,
)
def create_batch_tracking(
    batch: BatchTrackingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_batch_tracking_service(
        db=db,
        batch=batch,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[BatchTrackingResponse],
)
def get_all_batch_tracking(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_batch_tracking_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{batch_id}",
    response_model=BatchTrackingResponse,
)
def get_batch_tracking(
    batch_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_batch_tracking_service(
        db=db,
        batch_id=batch_id,
        current_user=current_user,
    )


@router.put(
    "/{batch_id}",
    response_model=BatchTrackingResponse,
)
def update_batch_tracking(
    batch_id: int,
    batch_update: BatchTrackingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_batch_tracking_service(
        db=db,
        batch_id=batch_id,
        batch_update=batch_update,
        current_user=current_user,
    )


@router.delete(
    "/{batch_id}",
)
def delete_batch_tracking(
    batch_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_batch_tracking_service(
        db=db,
        batch_id=batch_id,
        current_user=current_user,
    )