from sqlalchemy.orm import Session

from models.result_publishing import ResultPublishing


def create_result(
    db: Session,
    result: ResultPublishing,
):

    db.add(result)

    db.commit()

    db.refresh(result)

    return result


def get_all_results(
    db: Session,
):

    return (

        db.query(ResultPublishing)

        .filter(
            ResultPublishing.is_active == True
        )

        .all()

    )


def get_result_by_id(
    db: Session,
    result_id: int,
):

    return (

        db.query(ResultPublishing)

        .filter(
            ResultPublishing.id == result_id
        )

        .first()

    )


def get_result_count(
    db: Session,
):

    return db.query(
        ResultPublishing
    ).count()


def update_result(
    db: Session,
    result: ResultPublishing,
):

    db.commit()

    db.refresh(result)

    return result


def delete_result(
    db: Session,
    result: ResultPublishing,
):

    result.is_active = False

    db.commit()

    db.refresh(result)

    return result