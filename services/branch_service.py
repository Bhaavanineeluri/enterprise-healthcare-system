from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)

from models.branch import Branch
from models.user import User

from repositories.branch_repository import (
    create_branch,
    delete_branch,
    get_all_branches,
    get_branch_by_email,
    get_branch_by_id,
    get_branch_count,
    update_branch,
)

from repositories.hospital_repository import (
    get_hospital_by_id,
)

from schemas.branch_schema import (
    BranchCreate,
    BranchUpdate,
)

from services.audit_service import save_audit_log


def generate_branch_code(
    db: Session,
):

    count = get_branch_count(db)

    return f"BR{count + 1:06d}"


def create_branch_service(
    db: Session,
    branch: BranchCreate,
    current_user: User,
):

    hospital = get_hospital_by_id(
        db,
        branch.hospital_id,
    )

    if hospital is None:

        not_found(
            "Hospital not found."
        )

    existing = get_branch_by_email(
        db,
        branch.email,
    )

    if existing:

        bad_request(
            "Branch email already exists."
        )

    new_branch = Branch(

        branch_code=generate_branch_code(db),

        hospital_id=branch.hospital_id,

        branch_name=branch.branch_name,

        email=branch.email,

        phone=branch.phone,

        address=branch.address,

        city=branch.city,

        state=branch.state,

        country=branch.country,

        postal_code=branch.postal_code,
    )

    branch_data = create_branch(
        db,
        new_branch,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BRANCH",
        action="CREATE",
    )

    return branch_data


def get_all_branches_service(
    db: Session,
    current_user: User,
):

    return get_all_branches(db)


def get_branch_service(
    db: Session,
    branch_id: int,
    current_user: User,
):

    branch = get_branch_by_id(
        db,
        branch_id,
    )

    if branch is None:

        not_found(
            "Branch not found."
        )

    return branch


def update_branch_service(
    db: Session,
    branch_id: int,
    branch_update: BranchUpdate,
    current_user: User,
):

    branch = get_branch_by_id(
        db,
        branch_id,
    )

    if branch is None:

        not_found(
            "Branch not found."
        )

    update_data = branch_update.model_dump(
        exclude_unset=True
    )

    if (
        "email" in update_data
        and
        update_data["email"] != branch.email
    ):

        existing = get_branch_by_email(
            db,
            update_data["email"],
        )

        if existing:

            bad_request(
                "Branch email already exists."
            )

    for key, value in update_data.items():

        setattr(
            branch,
            key,
            value,
        )

    updated = update_branch(
        db,
        branch,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BRANCH",
        action="UPDATE",
    )

    return updated


def delete_branch_service(
    db: Session,
    branch_id: int,
    current_user: User,
):

    branch = get_branch_by_id(
        db,
        branch_id,
    )

    if branch is None:

        not_found(
            "Branch not found."
        )

    delete_branch(
        db,
        branch,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="BRANCH",
        action="DELETE",
    )

    return {
        "message": "Branch deleted successfully."
    }