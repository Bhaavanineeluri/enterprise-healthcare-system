from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.clinical_note_schema import (
    ClinicalNoteCreate,
    ClinicalNoteResponse,
    ClinicalNoteUpdate,
)

from services.clinical_note_service import (
    create_clinical_note_service,
    delete_clinical_note_service,
    get_all_clinical_notes_service,
    get_clinical_note_service,
    update_clinical_note_service,
)


router = APIRouter(
    prefix="/clinical-notes",
    tags=["Clinical Notes"],
)


@router.post(
    "/",
    response_model=ClinicalNoteResponse,
)
def create_clinical_note(
    clinical_note: ClinicalNoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_clinical_note_service(
        db=db,
        clinical_note=clinical_note,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[ClinicalNoteResponse],
)
def get_all_clinical_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_clinical_notes_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{clinical_note_id}",
    response_model=ClinicalNoteResponse,
)
def get_clinical_note(
    clinical_note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_clinical_note_service(
        db=db,
        clinical_note_id=clinical_note_id,
        current_user=current_user,
    )


@router.put(
    "/{clinical_note_id}",
    response_model=ClinicalNoteResponse,
)
def update_clinical_note(
    clinical_note_id: int,
    clinical_note_update: ClinicalNoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_clinical_note_service(
        db=db,
        clinical_note_id=clinical_note_id,
        clinical_note_update=clinical_note_update,
        current_user=current_user,
    )


@router.delete(
    "/{clinical_note_id}",
)
def delete_clinical_note(
    clinical_note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_clinical_note_service(
        db=db,
        clinical_note_id=clinical_note_id,
        current_user=current_user,
    )