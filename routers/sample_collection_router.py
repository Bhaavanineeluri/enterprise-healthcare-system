from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.sample_collection_schema import (
    SampleCollectionCreate,
    SampleCollectionResponse,
    SampleCollectionUpdate,
)

from services.sample_collection_service import (
    create_sample_collection_service,
    delete_sample_collection_service,
    get_all_sample_collections_service,
    get_sample_collection_service,
    update_sample_collection_service,
)


router = APIRouter(
    prefix="/sample-collections",
    tags=["Sample Collection"],
)


@router.post(
    "/",
    response_model=SampleCollectionResponse,
)
def create_sample_collection(
    sample_collection: SampleCollectionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_sample_collection_service(
        db=db,
        sample_collection=sample_collection,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[SampleCollectionResponse],
)
def get_all_sample_collections(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_sample_collections_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{sample_collection_id}",
    response_model=SampleCollectionResponse,
)
def get_sample_collection(
    sample_collection_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_sample_collection_service(
        db=db,
        sample_collection_id=sample_collection_id,
        current_user=current_user,
    )


@router.put(
    "/{sample_collection_id}",
    response_model=SampleCollectionResponse,
)
def update_sample_collection(
    sample_collection_id: int,
    sample_collection_update: SampleCollectionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_sample_collection_service(
        db=db,
        sample_collection_id=sample_collection_id,
        sample_collection_update=sample_collection_update,
        current_user=current_user,
    )


@router.delete(
    "/{sample_collection_id}",
)
def delete_sample_collection(
    sample_collection_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_sample_collection_service(
        db=db,
        sample_collection_id=sample_collection_id,
        current_user=current_user,
    )