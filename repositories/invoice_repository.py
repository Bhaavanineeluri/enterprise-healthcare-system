from sqlalchemy.orm import Session

from models.invoice import Invoice


def create_invoice(
    db: Session,
    invoice: Invoice,
):

    db.add(invoice)

    db.commit()

    db.refresh(invoice)

    return invoice


def get_all_invoices(
    db: Session,
):

    return (
        db.query(Invoice)
        .filter(
            Invoice.is_active == True
        )
        .all()
    )


def get_invoice_by_id(
    db: Session,
    invoice_id: int,
):

    return (
        db.query(Invoice)
        .filter(
            Invoice.id == invoice_id
        )
        .first()
    )


def get_invoice_count(
    db: Session,
):

    return db.query(
        Invoice
    ).count()


def update_invoice(
    db: Session,
    invoice: Invoice,
):

    db.commit()

    db.refresh(invoice)

    return invoice


def delete_invoice(
    db: Session,
    invoice: Invoice,
):

    invoice.is_active = False

    db.commit()

    db.refresh(invoice)

    return invoice