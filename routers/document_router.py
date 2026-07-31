from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.document_schema import (
    DocumentCreate,
    DocumentResponse,
    DocumentUpdate,
)

from services.document_service import (
    create_document_service,
    delete_document_service,
    get_all_documents_service,
    get_document_service,
    update_document_service,
)


router = APIRouter(
    prefix="/documents",
    tags=["Document Management"],
)


@router.post(
    "/",
    response_model=DocumentResponse,
)
def create_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_document_service(
        db=db,
        document=document,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[DocumentResponse],
)
def get_all_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_documents_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_document_service(
        db=db,
        document_id=document_id,
        current_user=current_user,
    )


@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
)
def update_document(
    document_id: int,
    document_update: DocumentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_document_service(
        db=db,
        document_id=document_id,
        document_update=document_update,
        current_user=current_user,
    )


@router.delete(
    "/{document_id}",
)
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_document_service(
        db=db,
        document_id=document_id,
        current_user=current_user,
    )