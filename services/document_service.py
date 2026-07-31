from sqlalchemy.orm import Session

from core.exceptions import (
    not_found,
)

from models.document import Document
from models.user import User

from repositories.patient_repository import (
    get_patient_by_id,
)

from repositories.document_repository import (
    create_document,
    delete_document,
    get_all_documents,
    get_document_by_id,
    get_document_count,
    update_document,
)

from schemas.document_schema import (
    DocumentCreate,
    DocumentUpdate,
)

from services.audit_service import (
    save_audit_log,
)


def generate_document_code(
    db: Session,
):

    count = get_document_count(db)

    return f"DOC{count + 1:06d}"


def create_document_service(
    db: Session,
    document: DocumentCreate,
    current_user: User,
):

    patient = get_patient_by_id(
        db,
        document.patient_id,
    )

    if patient is None:

        not_found(
            "Patient not found."
        )

    new_document = Document(

        document_code=generate_document_code(
            db,
        ),

        patient_id=document.patient_id,

        document_name=document.document_name,

        document_type=document.document_type,

        file_path=document.file_path,

        uploaded_by=current_user.id,

        uploaded_at=document.uploaded_at,

        remarks=document.remarks,
    )

    created = create_document(
        db,
        new_document,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DOCUMENT",
        action="CREATE",
    )

    return created


def get_all_documents_service(
    db: Session,
    current_user: User,
):

    return get_all_documents(
        db,
    )


def get_document_service(
    db: Session,
    document_id: int,
    current_user: User,
):

    document = get_document_by_id(
        db,
        document_id,
    )

    if document is None:

        not_found(
            "Document not found."
        )

    return document


def update_document_service(
    db: Session,
    document_id: int,
    document_update: DocumentUpdate,
    current_user: User,
):

    document = get_document_by_id(
        db,
        document_id,
    )

    if document is None:

        not_found(
            "Document not found."
        )

    update_data = document_update.model_dump(
        exclude_unset=True,
    )

    for key, value in update_data.items():

        setattr(
            document,
            key,
            value,
        )

    updated = update_document(
        db,
        document,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DOCUMENT",
        action="UPDATE",
    )

    return updated


def delete_document_service(
    db: Session,
    document_id: int,
    current_user: User,
):

    document = get_document_by_id(
        db,
        document_id,
    )

    if document is None:

        not_found(
            "Document not found."
        )

    delete_document(
        db,
        document,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DOCUMENT",
        action="DELETE",
    )

    return {
        "message": "Document deleted successfully."
    }