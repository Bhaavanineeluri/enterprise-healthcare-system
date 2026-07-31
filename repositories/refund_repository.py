from sqlalchemy.orm import Session

from models.refund import Refund


def create_refund(
    db: Session,
    refund: Refund,
):

    db.add(refund)

    db.commit()

    db.refresh(refund)

    return refund


def get_all_refunds(
    db: Session,
):

    return (
        db.query(Refund)
        .filter(
            Refund.is_active == True
        )
        .all()
    )


def get_refund_by_id(
    db: Session,
    refund_id: int,
):

    return (
        db.query(Refund)
        .filter(
            Refund.id == refund_id
        )
        .first()
    )


def get_refund_count(
    db: Session,
):

    return db.query(
        Refund
    ).count()


def update_refund(
    db: Session,
    refund: Refund,
):

    db.commit()

    db.refresh(refund)

    return refund


def delete_refund(
    db: Session,
    refund: Refund,
):

    refund.is_active = False

    db.commit()

    db.refresh(refund)

    return refund