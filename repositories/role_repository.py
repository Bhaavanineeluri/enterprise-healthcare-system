from sqlalchemy.orm import Session

from models.role import Role


def get_role_by_name(
    db: Session,
    role_name: str
):
    return (
        db.query(Role)
        .filter(Role.role_name == role_name)
        .first()
    )


def get_all_roles(
    db: Session
):
    return db.query(Role).all()


def create_role(
    db: Session,
    role: Role
):

    db.add(role)
    db.commit()
    db.refresh(role)

    return role