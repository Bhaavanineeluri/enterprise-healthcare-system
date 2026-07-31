from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.dependencies import get_db
from database.connection import SessionLocal
from dependencies.auth import get_current_user
from repositories.auth_repository import get_user_by_username


from core.security import verify_password
from models.user import User
from services.auth_service import complete_login_after_otp
from repositories.auth_repository import (
    get_all_devices,
    get_all_sessions,
    get_login_history,
)

from schemas.auth_schema import (
    LoginResponse,
    TokenResponse,
    UserRegister,
    UserResponse,
)

from schemas.otp_schema import (
    OTPRequest,
    OTPVerify,
    ForgotPasswordRequest,
    ResetPasswordRequest,
)

from services.auth_service import (
    login_user,
    logout_user,
    refresh_access_token,
    register_user,
)

from services.otp_service import (
    send_otp,
    verify_otp,
    reset_password,
)

from utils.rate_limiter import rate_limit



router = APIRouter(
    prefix="/auth",
    tags=["AUTHENTICATION"],
)




@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):

    try:

        return register_user(
            db,
            user,
        )


    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    rate_limit(request)


    try:

        return login_user(
            db=db,
            username=form_data.username,
            password=form_data.password,
        )


    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )




@router.post(
    "/verify-otp",
    response_model=TokenResponse,
)
def verify_login_otp(
    request: OTPVerify,
    db: Session = Depends(get_db),
):

    return verify_otp(
        db=db,
        email=request.email,
        otp_code=request.otp,
        purpose="LOGIN",
    )





@router.post(
    "/forgot-password",
)
def forgot_password(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db),
):

    return send_otp(
        db=db,
        email=request.email,
        purpose="RESET_PASSWORD",
    )

@router.post(
    "/reset-password",
)
def reset_password_api(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db),
):

    return reset_password(
        db=db,
        email=request.email,
        otp_code=request.otp,
        new_password=request.new_password,
    )


@router.post(
    "/token",
    response_model=TokenResponse,
)
def oauth2_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    try:

        user = get_user_by_username(
            db,
            form_data.username,
        )


        if user is None:

            raise HTTPException(
                status_code=400,
                detail="Invalid username or password"
            )


        if not verify_password(
            form_data.password,
            user.password,
        ):

            raise HTTPException(
                status_code=400,
                detail="Invalid username or password"
            )


        return complete_login_after_otp(
            db,
            user,
        )


    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/refresh-token",
)
def refresh_token(
    token: str,
    db: Session = Depends(get_db),
):

    try:

        return refresh_access_token(
            db,
            token,
        )


    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )




@router.post(
    "/logout",
)
def logout(
    token: str,
    db: Session = Depends(get_db),
):

    return logout_user(
        db,
        token,
    )





@router.get(
    "/current-user",
)
def current_user(
    current_user: User = Depends(get_current_user),
):

    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role.role_name,
    }





@router.get(
    "/sessions",
)
def sessions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_sessions(
        db,
        current_user.id,
    )





@router.get(
    "/devices",
)
def devices(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_devices(
        db,
        current_user.id,
    )





@router.get(
    "/login-history",
)
def login_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_login_history(
        db,
        current_user.id,
    )