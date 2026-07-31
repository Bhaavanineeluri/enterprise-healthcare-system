from sqlalchemy.orm import Session

from models.device import Device
from models.login_history import LoginHistory
from models.refresh_token import RefreshToken
from models.session import Session as UserSession
from models.user import User
from models.role import Role

def get_user_by_username(
    db: Session,
    username: str
):

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
    db: Session,
    user: User
):

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def save_refresh_token(
    db: Session,
    refresh: RefreshToken
):

    db.add(refresh)
    db.commit()
    db.refresh(refresh)

    return refresh


def get_refresh_token(
    db: Session,
    token: str
):

    return (
        db.query(RefreshToken)
        .filter(
            RefreshToken.token == token
        )
        .first()
    )


def delete_refresh_token(
    db: Session,
    refresh: RefreshToken
):

    db.delete(refresh)
    db.commit()


def create_session(
    db: Session,
    session_data: UserSession
):

    db.add(session_data)
    db.commit()
    db.refresh(session_data)

    return session_data


def create_device(
    db: Session,
    device: Device
):

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


def create_login_history(
    db: Session,
    history: LoginHistory
):

    db.add(history)
    db.commit()
    db.refresh(history)

    return history


def get_all_sessions(
    db: Session,
    user_id: int
):

    return (
        db.query(UserSession)
        .filter(UserSession.user_id == user_id)
        .all()
    )


def get_all_devices(
    db: Session,
    user_id: int
):

    return (
        db.query(Device)
        .filter(Device.user_id == user_id)
        .all()
    )


def get_login_history(
    db: Session,
    user_id: int
):

    return (
        db.query(LoginHistory)
        .filter(LoginHistory.user_id == user_id)
        .all()
    )
def get_role_by_name(
    db: Session,
    role_name: str
):

    return (
        db.query(Role)
        .filter(Role.role_name == role_name)
        .first()
    )