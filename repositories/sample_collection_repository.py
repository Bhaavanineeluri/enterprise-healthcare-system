from sqlalchemy.orm import Session

from models.sample_collection import SampleCollection


def create_sample_collection(
    db: Session,
    sample_collection: SampleCollection,
):

    db.add(sample_collection)

    db.commit()

    db.refresh(sample_collection)

    return sample_collection


def get_all_sample_collections(
    db: Session,
):

    return (

        db.query(SampleCollection)

        .filter(
            SampleCollection.is_active == True
        )

        .all()

    )


def get_sample_collection_by_id(
    db: Session,
    sample_collection_id: int,
):

    return (

        db.query(SampleCollection)

        .filter(
            SampleCollection.id == sample_collection_id
        )

        .first()

    )


def get_sample_collection_count(
    db: Session,
):

    return db.query(
        SampleCollection
    ).count()


def update_sample_collection(
    db: Session,
    sample_collection: SampleCollection,
):

    db.commit()

    db.refresh(sample_collection)

    return sample_collection


def delete_sample_collection(
    db: Session,
    sample_collection: SampleCollection,
):

    sample_collection.is_active = False

    db.commit()

    db.refresh(sample_collection)

    return sample_collection