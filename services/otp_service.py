import random

from datetime import datetime, timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.otp import OTP

from repositories.auth_repository import (
    get_user_by_email,
)

from repositories.otp_repository import (
    create_otp,
    get_latest_otp,
    update_otp,
)

from security.hashing import hash_password
from security.password_policy import validate_password



def generate_otp():

    return str(
        random.randint(100000, 999999)
    )




def send_otp(
    db: Session,
    email: str,
    purpose: str,
):

    user = get_user_by_email(
        db,
        email,
    )


    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )



    otp = OTP(
        user_id=user.id,
        otp_code=generate_otp(),
        purpose=purpose,
        expires_at=datetime.utcnow()
        + timedelta(minutes=5),
    )



    create_otp(
        db,
        otp,
    )



    return {
        "message": "OTP generated successfully.",
        "otp": otp.otp_code,
    }





def verify_otp(
    db: Session,
    email: str,
    otp_code: str,
    purpose: str,
):

    user = get_user_by_email(
        db,
        email,
    )


    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )



    otp = get_latest_otp(
        db,
        user.id,
        purpose,
    )



    if otp is None:

        raise HTTPException(
            status_code=404,
            detail="OTP not found.",
        )



    if otp.is_verified:

        raise HTTPException(
            status_code=400,
            detail="OTP already used.",
        )



    if otp.otp_code != otp_code:

        raise HTTPException(
            status_code=400,
            detail="Invalid OTP.",
        )



    if datetime.utcnow() > otp.expires_at:

        raise HTTPException(
            status_code=400,
            detail="OTP expired.",
        )



    otp.is_verified = True



    update_otp(
        db,
        otp,
    )



    # LOGIN MFA SUCCESS
    if purpose == "LOGIN":

        from services.auth_service import (
            complete_login_after_otp,
        )


        return complete_login_after_otp(
            db,
            user,
        )



    return {
        "message": "OTP verified successfully."
    }





def reset_password(
    db: Session,
    email: str,
    otp_code: str,
    new_password: str,
):

    validate_password(
        new_password,
    )



    user = get_user_by_email(
        db,
        email,
    )



    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found.",
        )



    otp = get_latest_otp(
        db,
        user.id,
        "RESET_PASSWORD",
    )



    if otp is None:

        raise HTTPException(
            status_code=404,
            detail="OTP not found.",
        )



    if otp.otp_code != otp_code:

        raise HTTPException(
            status_code=400,
            detail="Invalid OTP.",
        )



    if not otp.is_verified:

        raise HTTPException(
            status_code=400,
            detail="Verify OTP first.",
        )



    user.password = hash_password(
        new_password,
    )



    db.commit()



    return {
        "message": "Password reset successful."
    }