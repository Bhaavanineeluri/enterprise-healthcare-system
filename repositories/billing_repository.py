from sqlalchemy.orm import Session

from models.billing import Billing


def create_billing(
    db: Session,
    billing: Billing,
):

    db.add(billing)

    db.commit()

    db.refresh(billing)

    return billing


def get_all_billings(
    db: Session,
):

    return (

        db.query(Billing)

        .filter(
            Billing.is_active == True
        )

        .all()

    )


def get_billing_by_id(
    db: Session,
    billing_id: int,
):

    return (

        db.query(Billing)

        .filter(
            Billing.id == billing_id
        )

        .first()

    )


def get_billing_count(
    db: Session,
):

    return db.query(
        Billing
    ).count()


def update_billing(
    db: Session,
    billing: Billing,
):

    db.commit()

    db.refresh(billing)

    return billing


def delete_billing(
    db: Session,
    billing: Billing,
):

    billing.is_active = False

    db.commit()

    db.refresh(billing)

    return billing