from sqlalchemy.orm import Session

from models.discharge_summary import DischargeSummary


def create_discharge_summary(
    db: Session,
    discharge_summary: DischargeSummary,
):

    db.add(discharge_summary)

    db.commit()

    db.refresh(discharge_summary)

    return discharge_summary


def get_all_discharge_summaries(
    db: Session,
):

    return (

        db.query(DischargeSummary)

        .filter(
            DischargeSummary.is_active == True
        )

        .all()

    )


def get_discharge_summary_by_id(
    db: Session,
    discharge_summary_id: int,
):

    return (

        db.query(DischargeSummary)

        .filter(
            DischargeSummary.id == discharge_summary_id
        )

        .first()

    )


def get_discharge_summary_count(
    db: Session,
):

    return (

        db.query(DischargeSummary)

        .count()

    )


def update_discharge_summary(
    db: Session,
    discharge_summary: DischargeSummary,
):

    db.commit()

    db.refresh(discharge_summary)

    return discharge_summary


def delete_discharge_summary(
    db: Session,
    discharge_summary: DischargeSummary,
):

    discharge_summary.is_active = False

    db.commit()

    db.refresh(discharge_summary)

    return discharge_summary