from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.department import Department
from models.user import User

from repositories.branch_repository import (
    get_branch_by_id,
)

from repositories.department_repository import (
    create_department,
    delete_department,
    get_all_departments,
    get_department_by_email,
    get_department_by_id,
    get_department_count,
    update_department,
)

from schemas.department_schema import (
    DepartmentCreate,
    DepartmentUpdate,
)

from services.audit_service import save_audit_log


def generate_department_code(
    db: Session,
):

    count = get_department_count(db)

    return f"DEP{count + 1:06d}"


def create_department_service(
    db: Session,
    department: DepartmentCreate,
    current_user: User,
):

    branch = get_branch_by_id(
        db,
        department.branch_id,
    )

    if branch is None:

        not_found(
            "Branch not found."
        )

    if (
        department.email
        and
        get_department_by_email(
            db,
            department.email,
        )
    ):

        bad_request(
            "Department email already exists."
        )

    new_department = Department(

        department_code=generate_department_code(db),

        branch_id=department.branch_id,

        department_name=department.department_name,

        description=department.description,

        phone=department.phone,

        email=department.email,

        location=department.location,
    )

    department_data = create_department(
        db,
        new_department,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DEPARTMENT",
        action="CREATE",
    )

    return department_data


def get_all_departments_service(
    db: Session,
    current_user: User,
):

    return get_all_departments(db)


def get_department_service(
    db: Session,
    department_id: int,
    current_user: User,
):

    department = get_department_by_id(
        db,
        department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    return department


def update_department_service(
    db: Session,
    department_id: int,
    department_update: DepartmentUpdate,
    current_user: User,
):

    department = get_department_by_id(
        db,
        department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    update_data = department_update.model_dump(
        exclude_unset=True
    )

    if (
        "email" in update_data
        and
        update_data["email"] != department.email
    ):

        existing = get_department_by_email(
            db,
            update_data["email"],
        )

        if existing:

            bad_request(
                "Department email already exists."
            )

    for key, value in update_data.items():

        setattr(
            department,
            key,
            value,
        )

    updated = update_department(
        db,
        department,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DEPARTMENT",
        action="UPDATE",
    )

    return updated


def delete_department_service(
    db: Session,
    department_id: int,
    current_user: User,
):

    department = get_department_by_id(
        db,
        department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    delete_department(
        db,
        department,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="DEPARTMENT",
        action="DELETE",
    )

    return {
        "message": "Department deleted successfully."
    }