from sqlalchemy.orm import Session

from models.ipd import IPD


def create_ipd(
    db: Session,
    ipd: IPD,
):

    db.add(ipd)

    db.commit()

    db.refresh(ipd)

    return ipd


def get_all_ipd(
    db: Session,
):

    return (

        db.query(IPD)

        .filter(
            IPD.is_active == True
        )

        .all()

    )


def get_ipd_by_id(
    db: Session,
    ipd_id: int,
):

    return (

        db.query(IPD)

        .filter(
            IPD.id == ipd_id
        )

        .first()

    )


def get_ipd_by_bed(
    db: Session,
    bed_id: int,
):

    return (

        db.query(IPD)

        .filter(
            IPD.bed_id == bed_id,
            IPD.status == "ADMITTED",
            IPD.is_active == True,
        )

        .first()

    )


def get_ipd_count(
    db: Session,
):

    return (

        db.query(IPD)

        .count()

    )


def update_ipd(
    db: Session,
    ipd: IPD,
):

    db.commit()

    db.refresh(ipd)

    return ipd


def delete_ipd(
    db: Session,
    ipd: IPD,
):

    ipd.is_active = False

    db.commit()

    db.refresh(ipd)

    return ipd