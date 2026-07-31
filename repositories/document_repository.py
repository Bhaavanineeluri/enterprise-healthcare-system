from sqlalchemy.orm import Session

from models.document import Document


def create_document(
    db: Session,
    document: Document,
):

    db.add(document)

    db.commit()

    db.refresh(document)

    return document


def get_all_documents(
    db: Session,
):

    return (
        db.query(Document)
        .filter(
            Document.is_active == True
        )
        .all()
    )


def get_document_by_id(
    db: Session,
    document_id: int,
):

    return (
        db.query(Document)
        .filter(
            Document.id == document_id
        )
        .first()
    )


def get_document_count(
    db: Session,
):

    return db.query(
        Document
    ).count()


def update_document(
    db: Session,
    document: Document,
):

    db.commit()

    db.refresh(document)

    return document


def delete_document(
    db: Session,
    document: Document,
):

    document.is_active = False

    db.commit()

    db.refresh(document)

    return document