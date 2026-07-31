from sqlalchemy.orm import Session

from models.payment import Payment


def create_payment(
    db: Session,
    payment: Payment,
):

    db.add(payment)

    db.commit()

    db.refresh(payment)

    return payment


def get_all_payments(
    db: Session,
):

    return (
        db.query(Payment)
        .filter(
            Payment.is_active == True
        )
        .all()
    )


def get_payment_by_id(
    db: Session,
    payment_id: int,
):

    return (
        db.query(Payment)
        .filter(
            Payment.id == payment_id
        )
        .first()
    )


def get_payment_count(
    db: Session,
):

    return db.query(
        Payment
    ).count()


def update_payment(
    db: Session,
    payment: Payment,
):

    db.commit()

    db.refresh(payment)

    return payment


def delete_payment(
    db: Session,
    payment: Payment,
):

    payment.is_active = False

    db.commit()

    db.refresh(payment)

    return payment