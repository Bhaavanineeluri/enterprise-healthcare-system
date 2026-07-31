from sqlalchemy.orm import Session

from models.test_processing import TestProcessing


def create_test_processing(
    db: Session,
    processing: TestProcessing,
):

    db.add(processing)

    db.commit()

    db.refresh(processing)

    return processing


def get_all_test_processing(
    db: Session,
):

    return (

        db.query(TestProcessing)

        .filter(
            TestProcessing.is_active == True
        )

        .all()

    )


def get_test_processing_by_id(
    db: Session,
    processing_id: int,
):

    return (

        db.query(TestProcessing)

        .filter(
            TestProcessing.id == processing_id
        )

        .first()

    )


def get_test_processing_count(
    db: Session,
):

    return db.query(
        TestProcessing
    ).count()


def update_test_processing(
    db: Session,
    processing: TestProcessing,
):

    db.commit()

    db.refresh(processing)

    return processing


def delete_test_processing(
    db: Session,
    processing: TestProcessing,
):

    processing.is_active = False

    db.commit()

    db.refresh(processing)

    return processing