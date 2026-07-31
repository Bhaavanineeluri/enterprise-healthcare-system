from sqlalchemy.orm import Session

from models.lab_order import LabOrder


def create_lab_order(
    db: Session,
    lab_order: LabOrder,
):

    db.add(lab_order)

    db.commit()

    db.refresh(lab_order)

    return lab_order


def get_all_lab_orders(
    db: Session,
):

    return (

        db.query(LabOrder)

        .filter(
            LabOrder.is_active == True
        )

        .all()

    )


def get_lab_order_by_id(
    db: Session,
    lab_order_id: int,
):

    return (

        db.query(LabOrder)

        .filter(
            LabOrder.id == lab_order_id
        )

        .first()

    )


def get_lab_order_count(
    db: Session,
):

    return db.query(LabOrder).count()


def update_lab_order(
    db: Session,
    lab_order: LabOrder,
):

    db.commit()

    db.refresh(lab_order)

    return lab_order


def delete_lab_order(
    db: Session,
    lab_order: LabOrder,
):

    lab_order.is_active = False

    db.commit()

    db.refresh(lab_order)

    return lab_order