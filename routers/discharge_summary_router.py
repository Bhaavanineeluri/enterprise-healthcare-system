from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.discharge_summary_schema import (
    DischargeSummaryCreate,
    DischargeSummaryResponse,
    DischargeSummaryUpdate,
)

from services.discharge_summary_service import (
    create_discharge_summary_service,
    get_all_discharge_summaries_service,
    get_discharge_summary_service,
    update_discharge_summary_service,
    delete_discharge_summary_service,
)


router = APIRouter(
    prefix="/discharge-summaries",
    tags=["Discharge Summary Management"],
)


@router.post(
    "/",
    response_model=DischargeSummaryResponse,
)
def create_discharge_summary(
    discharge_summary: DischargeSummaryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_discharge_summary_service(
        db=db,
        discharge_summary=discharge_summary,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[DischargeSummaryResponse],
)
def get_all_discharge_summaries(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_discharge_summaries_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{discharge_summary_id}",
    response_model=DischargeSummaryResponse,
)
def get_discharge_summary(
    discharge_summary_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_discharge_summary_service(
        db=db,
        discharge_summary_id=discharge_summary_id,
        current_user=current_user,
    )


@router.put(
    "/{discharge_summary_id}",
    response_model=DischargeSummaryResponse,
)
def update_discharge_summary(
    discharge_summary_id: int,
    discharge_summary_update: DischargeSummaryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_discharge_summary_service(
        db=db,
        discharge_summary_id=discharge_summary_id,
        discharge_summary_update=discharge_summary_update,
        current_user=current_user,
    )


@router.delete(
    "/{discharge_summary_id}",
)
def delete_discharge_summary(
    discharge_summary_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_discharge_summary_service(
        db=db,
        discharge_summary_id=discharge_summary_id,
        current_user=current_user,
    )