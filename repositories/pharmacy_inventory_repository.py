from sqlalchemy.orm import Session

from models.pharmacy_inventory import PharmacyInventory


def create_pharmacy_inventory(
    db: Session,
    inventory: PharmacyInventory,
):

    db.add(inventory)

    db.commit()

    db.refresh(inventory)

    return inventory


def get_all_pharmacy_inventory(
    db: Session,
):

    return (

        db.query(PharmacyInventory)

        .filter(
            PharmacyInventory.is_active == True
        )

        .all()

    )


def get_pharmacy_inventory_by_id(
    db: Session,
    inventory_id: int,
):

    return (

        db.query(PharmacyInventory)

        .filter(
            PharmacyInventory.id == inventory_id
        )

        .first()

    )


def get_pharmacy_inventory_by_batch(
    db: Session,
    batch_number: str,
):

    return (

        db.query(PharmacyInventory)

        .filter(
            PharmacyInventory.batch_number == batch_number
        )

        .first()

    )


def get_pharmacy_inventory_count(
    db: Session,
):

    return db.query(
        PharmacyInventory
    ).count()


def update_pharmacy_inventory(
    db: Session,
    inventory: PharmacyInventory,
):

    db.commit()

    db.refresh(inventory)

    return inventory


def delete_pharmacy_inventory(
    db: Session,
    inventory: PharmacyInventory,
):

    inventory.is_active = False

    db.commit()

    db.refresh(inventory)

    return inventory