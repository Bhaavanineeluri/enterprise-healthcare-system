from sqlalchemy.orm import Session

from models.otp import OTP


def create_otp(
    db: Session,
    otp: OTP,
):
    db.add(otp)
    db.commit()
    db.refresh(otp)

    return otp


def get_latest_otp(
    db: Session,
    user_id: int,
    purpose: str,
):
    return (
        db.query(OTP)
        .filter(
            OTP.user_id == user_id,
            OTP.purpose == purpose,
        )
        .order_by(OTP.id.desc())
        .first()
    )


def update_otp(
    db: Session,
    otp: OTP,
):
    db.commit()
    db.refresh(otp)

    return otp


def delete_otp(
    db: Session,
    otp: OTP,
):
    db.delete(otp)
    db.commit()