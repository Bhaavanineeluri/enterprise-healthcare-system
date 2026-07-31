from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.treatment_plan_schema import (
    TreatmentPlanCreate,
    TreatmentPlanResponse,
    TreatmentPlanUpdate,
)

from services.treatment_plan_service import (
    create_treatment_plan_service,
    get_all_treatment_plans_service,
    get_treatment_plan_service,
    update_treatment_plan_service,
    delete_treatment_plan_service,
)


router = APIRouter(
    prefix="/treatment-plans",
    tags=["Treatment Plan Management"],
)


@router.post(
    "/",
    response_model=TreatmentPlanResponse,
)
def create_treatment_plan(
    treatment_plan: TreatmentPlanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_treatment_plan_service(
        db=db,
        treatment_plan=treatment_plan,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[TreatmentPlanResponse],
)
def get_all_treatment_plans(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_treatment_plans_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{treatment_plan_id}",
    response_model=TreatmentPlanResponse,
)
def get_treatment_plan(
    treatment_plan_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_treatment_plan_service(
        db=db,
        treatment_plan_id=treatment_plan_id,
        current_user=current_user,
    )


@router.put(
    "/{treatment_plan_id}",
    response_model=TreatmentPlanResponse,
)
def update_treatment_plan(
    treatment_plan_id: int,
    treatment_plan_update: TreatmentPlanUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_treatment_plan_service(
        db=db,
        treatment_plan_id=treatment_plan_id,
        treatment_plan_update=treatment_plan_update,
        current_user=current_user,
    )


@router.delete(
    "/{treatment_plan_id}",
)
def delete_treatment_plan(
    treatment_plan_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_treatment_plan_service(
        db=db,
        treatment_plan_id=treatment_plan_id,
        current_user=current_user,
    )