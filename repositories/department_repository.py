from sqlalchemy.orm import Session

from models.department import Department


def create_department(
    db: Session,
    department: Department,
):

    db.add(department)

    db.commit()

    db.refresh(department)

    return department


def get_all_departments(
    db: Session,
):

    return (

        db.query(Department)

        .filter(
            Department.is_active == True
        )

        .all()

    )


def get_department_by_id(
    db: Session,
    department_id: int,
):

    return (

        db.query(Department)

        .filter(
            Department.id == department_id
        )

        .first()

    )


def get_department_by_code(
    db: Session,
    department_code: str,
):

    return (

        db.query(Department)

        .filter(
            Department.department_code == department_code
        )

        .first()

    )


def get_department_by_email(
    db: Session,
    email: str,
):

    return (

        db.query(Department)

        .filter(
            Department.email == email
        )

        .first()

    )


def get_departments_by_branch(
    db: Session,
    branch_id: int,
):

    return (

        db.query(Department)

        .filter(
            Department.branch_id == branch_id,
            Department.is_active == True
        )

        .all()

    )


def update_department(
    db: Session,
    department: Department,
):

    db.commit()

    db.refresh(department)

    return department


def delete_department(
    db: Session,
    department: Department,
):

    department.is_active = False

    db.commit()

    db.refresh(department)

    return department


def get_department_count(
    db: Session,
):

    return (

        db.query(Department)

        .count()

    )