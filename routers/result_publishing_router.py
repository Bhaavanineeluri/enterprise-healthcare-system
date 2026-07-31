from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.result_publishing_schema import (
    ResultPublishingCreate,
    ResultPublishingResponse,
    ResultPublishingUpdate,
)

from services.result_publishing_service import (
    create_result_service,
    delete_result_service,
    get_all_results_service,
    get_result_service,
    update_result_service,
)


router = APIRouter(
    prefix="/result-publishing",
    tags=["Result Publishing"],
)


@router.post(
    "/",
    response_model=ResultPublishingResponse,
)
def create_result(
    result: ResultPublishingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_result_service(
        db=db,
        result=result,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[ResultPublishingResponse],
)
def get_all_results(
    db: Session = Depends(get_db),
):

    return get_all_results_service(
        db=db,
    )


@router.get(
    "/{result_id}",
    response_model=ResultPublishingResponse,
)
def get_result(
    result_id: int,
    db: Session = Depends(get_db),
):

    return get_result_service(
        db=db,
        result_id=result_id,
    )


@router.put(
    "/{result_id}",
    response_model=ResultPublishingResponse,
)
def update_result(
    result_id: int,
    result_update: ResultPublishingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_result_service(
        db=db,
        result_id=result_id,
        result_update=result_update,
        current_user=current_user,
    )


@router.delete(
    "/{result_id}",
)
def delete_result(
    result_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_result_service(
        db=db,
        result_id=result_id,
        current_user=current_user,
    )