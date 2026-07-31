from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from core.dependencies import get_db
from models.user import User
from utils.jwt_handler import verify_token



oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)




def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):

    try:

        payload = verify_token(
            token
        )


        if payload is None:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
                headers={
                    "WWW-Authenticate": "Bearer"
                },
            )


        username = payload.get(
            "sub"
        )


        if username is None:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
                headers={
                    "WWW-Authenticate": "Bearer"
                },
            )


        user = (
            db.query(User)
            .filter(
                User.username == username
            )
            .first()
        )


        if user is None:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={
                    "WWW-Authenticate": "Bearer"
                },
            )


        return user



    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={
                "WWW-Authenticate": "Bearer"
            },
        )





def require_roles(*roles):

    def role_checker(
        current_user: User = Depends(get_current_user),
    ):


        if current_user.role.role_name not in roles:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )


        return current_user


    return role_checker