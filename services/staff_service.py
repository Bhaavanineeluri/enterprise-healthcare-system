from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.staff import Staff
from models.user import User

from repositories.department_repository import (
    get_department_by_id,
)

from repositories.staff_repository import (
    create_staff,
    delete_staff,
    get_all_staff,
    get_staff_by_email,
    get_staff_by_id,
    get_staff_count,
    update_staff,
)

from schemas.staff_schema import (
    StaffCreate,
    StaffUpdate,
)

from services.audit_service import save_audit_log


def generate_staff_code(
    db: Session,
):

    count = get_staff_count(db)

    return f"STF{count + 1:06d}"


def create_staff_service(
    db: Session,
    staff: StaffCreate,
    current_user: User,
):

    department = get_department_by_id(
        db,
        staff.department_id,
    )

    if department is None:

        not_found(
            "Department not found."
        )

    existing = get_staff_by_email(
        db,
        staff.email,
    )

    if existing:

        bad_request(
            "Staff email already exists."
        )

    new_staff = Staff(

        staff_code=generate_staff_code(db),

        department_id=staff.department_id,

        first_name=staff.first_name,

        last_name=staff.last_name,

        gender=staff.gender,

        designation=staff.designation,

        employee_type=staff.employee_type,

        qualification=staff.qualification,

        email=staff.email,

        phone=staff.phone,

        joining_date=staff.joining_date,
    )

    staff_data = create_staff(
        db,
        new_staff,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="STAFF",
        action="CREATE",
    )

    return staff_data


def get_all_staff_service(
    db: Session,
    current_user: User,
):

    return get_all_staff(db)


def get_staff_service(
    db: Session,
    staff_id: int,
    current_user: User,
):

    staff = get_staff_by_id(
        db,
        staff_id,
    )

    if staff is None:

        not_found(
            "Staff not found."
        )

    return staff


def update_staff_service(
    db: Session,
    staff_id: int,
    staff_update: StaffUpdate,
    current_user: User,
):

    staff = get_staff_by_id(
        db,
        staff_id,
    )

    if staff is None:

        not_found(
            "Staff not found."
        )

    update_data = staff_update.model_dump(
        exclude_unset=True
    )

    if "department_id" in update_data:

        department = get_department_by_id(
            db,
            update_data["department_id"],
        )

        if department is None:

            not_found(
                "Department not found."
            )

    if (
        "email" in update_data
        and
        update_data["email"] != staff.email
    ):

        existing = get_staff_by_email(
            db,
            update_data["email"],
        )

        if existing:

            bad_request(
                "Staff email already exists."
            )

    for key, value in update_data.items():

        setattr(
            staff,
            key,
            value,
        )

    updated = update_staff(
        db,
        staff,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="STAFF",
        action="UPDATE",
    )

    return updated


def delete_staff_service(
    db: Session,
    staff_id: int,
    current_user: User,
):

    staff = get_staff_by_id(
        db,
        staff_id,
    )

    if staff is None:

        not_found(
            "Staff not found."
        )

    delete_staff(
        db,
        staff,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="STAFF",
        action="DELETE",
    )

    return {
        "message": "Staff deleted successfully."
    }