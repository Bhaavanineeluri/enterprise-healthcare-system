from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.test_processing_schema import (
    TestProcessingCreate,
    TestProcessingResponse,
    TestProcessingUpdate,
)

from services.test_processing_service import (
    create_test_processing_service,
    delete_test_processing_service,
    get_all_test_processing_service,
    get_test_processing_service,
    update_test_processing_service,
)


router = APIRouter(
    prefix="/test-processing",
    tags=["Test Processing"],
)


@router.post(
    "/",
    response_model=TestProcessingResponse,
)
def create_test_processing(
    processing: TestProcessingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_test_processing_service(
        db=db,
        processing=processing,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[TestProcessingResponse],
)
def get_all_test_processing(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_test_processing_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{processing_id}",
    response_model=TestProcessingResponse,
)
def get_test_processing(
    processing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_test_processing_service(
        db=db,
        processing_id=processing_id,
        current_user=current_user,
    )


@router.put(
    "/{processing_id}",
    response_model=TestProcessingResponse,
)
def update_test_processing(
    processing_id: int,
    processing_update: TestProcessingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_test_processing_service(
        db=db,
        processing_id=processing_id,
        processing_update=processing_update,
        current_user=current_user,
    )


@router.delete(
    "/{processing_id}",
)
def delete_test_processing(
    processing_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_test_processing_service(
        db=db,
        processing_id=processing_id,
        current_user=current_user,
    )