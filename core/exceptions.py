from fastapi import HTTPException
from fastapi import status


def bad_request(
    message: str,
):

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    )


def unauthorized(
    message: str = "Unauthorized",
):

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message,
    )


def forbidden(
    message: str = "Access denied",
):

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=message,
    )


def not_found(
    message: str,
):

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=message,
    )


def conflict(
    message: str,
):

    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=message,
    )


def internal_server_error(
    message: str = "Internal Server Error",
):

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=message,
    )