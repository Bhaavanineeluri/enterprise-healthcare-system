from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from core.dependencies import (
    get_db
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.branch_schema import (
    BranchCreate,
    BranchUpdate,
    BranchResponse,
)

from services.branch_service import (
    create_branch_service,
    get_all_branches_service,
    get_branch_service,
    update_branch_service,
    delete_branch_service,
)


router = APIRouter(
    prefix="/branches",
    tags=["Branch Management"],
)


@router.post(
    "/",
    response_model=BranchResponse,
)
def create_branch(
    branch: BranchCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_branch_service(
        db=db,
        branch=branch,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[BranchResponse],
)
def get_all_branches(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_branches_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{branch_id}",
    response_model=BranchResponse,
)
def get_branch(
    branch_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_branch_service(
        db=db,
        branch_id=branch_id,
        current_user=current_user,
    )


@router.put(
    "/{branch_id}",
    response_model=BranchResponse,
)
def update_branch(
    branch_id: int,
    branch_update: BranchUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_branch_service(
        db=db,
        branch_id=branch_id,
        branch_update=branch_update,
        current_user=current_user,
    )


@router.delete(
    "/{branch_id}",
)
def delete_branch(
    branch_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_branch_service(
        db=db,
        branch_id=branch_id,
        current_user=current_user,
    )