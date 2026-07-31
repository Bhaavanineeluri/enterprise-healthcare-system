from sqlalchemy.orm import Session

from models.branch import Branch


def create_branch(
    db: Session,
    branch: Branch,
):

    db.add(branch)

    db.commit()

    db.refresh(branch)

    return branch


def get_all_branches(
    db: Session,
):

    return (

        db.query(Branch)

        .filter(
            Branch.is_active == True
        )

        .all()

    )


def get_branch_by_id(
    db: Session,
    branch_id: int,
):

    return (

        db.query(Branch)

        .filter(
            Branch.id == branch_id
        )

        .first()

    )


def get_branch_by_code(
    db: Session,
    branch_code: str,
):

    return (

        db.query(Branch)

        .filter(
            Branch.branch_code == branch_code
        )

        .first()

    )


def get_branch_by_email(
    db: Session,
    email: str,
):

    return (

        db.query(Branch)

        .filter(
            Branch.email == email
        )

        .first()

    )


def get_branches_by_hospital(
    db: Session,
    hospital_id: int,
):

    return (

        db.query(Branch)

        .filter(
            Branch.hospital_id == hospital_id,
            Branch.is_active == True
        )

        .all()

    )


def update_branch(
    db: Session,
    branch: Branch,
):

    db.commit()

    db.refresh(branch)

    return branch


def delete_branch(
    db: Session,
    branch: Branch,
):

    branch.is_active = False

    db.commit()

    db.refresh(branch)

    return branch


def get_branch_count(
    db: Session,
):

    return (

        db.query(Branch)

        .count()

    )