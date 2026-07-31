from sqlalchemy.orm import Session

from models.medicine_dispensing import MedicineDispensing


def create_medicine_dispensing(
    db: Session,
    dispensing: MedicineDispensing,
):

    db.add(dispensing)

    db.commit()

    db.refresh(dispensing)

    return dispensing


def get_all_medicine_dispensings(
    db: Session,
):

    return (

        db.query(MedicineDispensing)

        .filter(
            MedicineDispensing.is_active == True
        )

        .all()

    )


def get_medicine_dispensing_by_id(
    db: Session,
    dispensing_id: int,
):

    return (

        db.query(MedicineDispensing)

        .filter(
            MedicineDispensing.id == dispensing_id
        )

        .first()

    )


def get_medicine_dispensing_count(
    db: Session,
):

    return db.query(
        MedicineDispensing
    ).count()


def update_medicine_dispensing(
    db: Session,
    dispensing: MedicineDispensing,
):

    db.commit()

    db.refresh(dispensing)

    return dispensing


def delete_medicine_dispensing(
    db: Session,
    dispensing: MedicineDispensing,
):

    dispensing.is_active = False

    db.commit()

    db.refresh(dispensing)

    return dispensing