from sqlalchemy.orm import Session

from models.drug_stock_management import DrugStockManagement


def create_drug_stock_management(
    db: Session,
    stock: DrugStockManagement,
):

    db.add(stock)

    db.commit()

    db.refresh(stock)

    return stock


def get_all_drug_stock_management(
    db: Session,
):

    return (
        db.query(DrugStockManagement)
        .filter(
            DrugStockManagement.is_active == True
        )
        .all()
    )


def get_drug_stock_management_by_id(
    db: Session,
    stock_id: int,
):

    return (
        db.query(DrugStockManagement)
        .filter(
            DrugStockManagement.id == stock_id
        )
        .first()
    )


def get_drug_stock_management_count(
    db: Session,
):

    return db.query(
        DrugStockManagement
    ).count()


def update_drug_stock_management(
    db: Session,
    stock: DrugStockManagement,
):

    db.commit()

    db.refresh(stock)

    return stock


def delete_drug_stock_management(
    db: Session,
    stock: DrugStockManagement,
):

    stock.is_active = False

    db.commit()

    db.refresh(stock)

    return stock