from sqlalchemy.orm import Session

from models.batch_tracking import BatchTracking


def create_batch_tracking(
    db: Session,
    batch: BatchTracking,
):

    db.add(batch)

    db.commit()

    db.refresh(batch)

    return batch


def get_all_batch_tracking(
    db: Session,
):

    return (
        db.query(BatchTracking)
        .filter(
            BatchTracking.is_active == True
        )
        .all()
    )


def get_batch_tracking_by_id(
    db: Session,
    batch_id: int,
):

    return (
        db.query(BatchTracking)
        .filter(
            BatchTracking.id == batch_id
        )
        .first()
    )


def get_batch_tracking_count(
    db: Session,
):

    return db.query(
        BatchTracking
    ).count()


def update_batch_tracking(
    db: Session,
    batch: BatchTracking,
):

    db.commit()

    db.refresh(batch)

    return batch


def delete_batch_tracking(
    db: Session,
    batch: BatchTracking,
):

    batch.is_active = False

    db.commit()

    db.refresh(batch)

    return batch