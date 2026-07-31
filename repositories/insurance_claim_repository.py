from sqlalchemy.orm import Session

from models.insurance_claim import InsuranceClaim


def create_insurance_claim(
    db: Session,
    claim: InsuranceClaim,
):

    db.add(claim)

    db.commit()

    db.refresh(claim)

    return claim


def get_all_insurance_claims(
    db: Session,
):

    return (
        db.query(InsuranceClaim)
        .filter(
            InsuranceClaim.is_active == True
        )
        .all()
    )


def get_insurance_claim_by_id(
    db: Session,
    claim_id: int,
):

    return (
        db.query(InsuranceClaim)
        .filter(
            InsuranceClaim.id == claim_id
        )
        .first()
    )


def get_insurance_claim_count(
    db: Session,
):

    return db.query(
        InsuranceClaim
    ).count()


def update_insurance_claim(
    db: Session,
    claim: InsuranceClaim,
):

    db.commit()

    db.refresh(claim)

    return claim


def delete_insurance_claim(
    db: Session,
    claim: InsuranceClaim,
):

    claim.is_active = False

    db.commit()

    db.refresh(claim)

    return claim