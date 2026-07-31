from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from config.settings import settings

from models.device import Device
from models.login_history import LoginHistory
from models.refresh_token import RefreshToken
from models.session import Session as UserSession
from models.user import User

from repositories.auth_repository import (
    create_user,
    delete_refresh_token,
    get_refresh_token,
    get_user_by_email,
    get_user_by_username,
    get_role_by_name,
    save_refresh_token,
)
from schemas.auth_schema import UserRegister

from security.hashing import (
    hash_password,
    verify_password,
)

from utils.jwt_handler import (
    create_access_token,
    create_refresh_token,
    verify_token,
)

from services.audit_service import save_audit_log
from services.otp_service import send_otp



def register_user(
    db: Session,
    user: UserRegister
):

    if get_user_by_username(db, user.username):
        raise ValueError(
            "Username already exists."
        )


    if get_user_by_email(db, user.email):
        raise ValueError(
            "Email already exists."
        )


    role = get_role_by_name(
        db,
        user.role_name
    )

    if role is None:
        raise ValueError(
            "Invalid role."
        )

    new_user = User(
        full_name=user.full_name,
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role_id=role.id,
    )

    created_user = create_user(
        db,
        new_user,
    )


    save_audit_log(
        db=db,
        current_user=created_user,
        module="AUTHENTICATION",
        action="REGISTER",
    )


    return created_user




def login_user(
    db: Session,
    username: str,
    password: str,
):

    db_user = get_user_by_username(
        db,
        username,
    )


    if db_user is None:
        raise ValueError(
            "Invalid Username or Password."
        )


    if not verify_password(
        password,
        db_user.password,
    ):
        raise ValueError(
            "Invalid Username or Password."
        )


    otp_response = send_otp(
        db=db,
        email=db_user.email,
        purpose="LOGIN",
    )


    return {
        "message": "OTP generated successfully.",
        "otp": otp_response["otp"]
    }




def complete_login_after_otp(
    db: Session,
    user: User,
):

    access_token = create_access_token(
        {
            "sub": user.username,
            "role": user.role.role_name,
        }
    )


    refresh_token = create_refresh_token(
        {
            "sub": user.username,
        }
    )


    refresh = RefreshToken(
        token=refresh_token,
        user_id=user.id,
        expires_at=datetime.now(timezone.utc)
        + timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS
        ),
    )


    save_refresh_token(
        db,
        refresh,
    )


    session = UserSession(
        user_id=user.id,
    )

    db.add(session)

    device = Device(
        user_id=user.id,
        device_name="MacBook Air",
        ip_address="127.0.0.1",
        browser="Safari",
        operating_system="Mac OS",
    )

    db.add(device)


    history = LoginHistory(
        user_id=user.id,
        status="SUCCESS",
    )

    db.add(history)


    db.commit()


    save_audit_log(
        db=db,
        current_user=user,
        module="AUTHENTICATION",
        action="LOGIN",
    )


    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }




def refresh_access_token(
    db: Session,
    token: str,
):

    payload = verify_token(token)


    if payload is None:
        raise ValueError(
            "Invalid Refresh Token."
        )


    db_token = get_refresh_token(
        db,
        token,
    )


    if db_token is None:
        raise ValueError(
            "Refresh Token Not Found."
        )


    access = create_access_token(
        {
            "sub": payload["sub"],
            "role": payload.get("role"),
        }
    )


    return {
        "access_token": access,
        "token_type": "bearer",
    }




def logout_user(
    db: Session,
    token: str,
):

    refresh = get_refresh_token(
        db,
        token,
    )


    if refresh:
        delete_refresh_token(
            db,
            refresh,
        )


    return {
        "message": "Logout successful."
    }