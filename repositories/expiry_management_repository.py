from sqlalchemy.orm import Session

from models.expiry_management import ExpiryManagement


def create_expiry_management(
    db: Session,
    expiry: ExpiryManagement,
):

    db.add(expiry)

    db.commit()

    db.refresh(expiry)

    return expiry


def get_all_expiry_management(
    db: Session,
):

    return (
        db.query(ExpiryManagement)
        .filter(
            ExpiryManagement.is_active == True
        )
        .all()
    )


def get_expiry_management_by_id(
    db: Session,
    expiry_id: int,
):

    return (
        db.query(ExpiryManagement)
        .filter(
            ExpiryManagement.id == expiry_id
        )
        .first()
    )


def get_expiry_management_count(
    db: Session,
):

    return db.query(
        ExpiryManagement
    ).count()


def update_expiry_management(
    db: Session,
    expiry: ExpiryManagement,
):

    db.commit()

    db.refresh(expiry)

    return expiry


def delete_expiry_management(
    db: Session,
    expiry: ExpiryManagement,
):

    expiry.is_active = False

    db.commit()

    db.refresh(expiry)

    return expiry