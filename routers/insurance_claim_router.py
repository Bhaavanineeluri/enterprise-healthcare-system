from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from core.dependencies import (
    get_db,
)
from dependencies.auth import get_current_user
from models.user import User

from schemas.insurance_claim_schema import (
    InsuranceClaimCreate,
    InsuranceClaimResponse,
    InsuranceClaimUpdate,
    ClaimApprovalRequest
)

from services.insurance_claim_service import (
    create_insurance_claim_service,
    delete_insurance_claim_service,
    get_all_insurance_claims_service,
    get_insurance_claim_service,
    approve_insurance_claim_service,
    update_insurance_claim_service,
)


router = APIRouter(
    prefix="/insurance-claims",
    tags=["Insurance Claims"],
)


@router.post(
    "/",
    response_model=InsuranceClaimResponse,
)
def create_insurance_claim(
    claim: InsuranceClaimCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_insurance_claim_service(
        db=db,
        claim=claim,
        current_user=current_user,
    )


@router.get(
    "/",
    response_model=list[InsuranceClaimResponse],
)
def get_all_insurance_claims(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_all_insurance_claims_service(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{claim_id}",
    response_model=InsuranceClaimResponse,
)
def get_insurance_claim(
    claim_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_insurance_claim_service(
        db=db,
        claim_id=claim_id,
        current_user=current_user,
    )


@router.put(
    "/{claim_id}",
    response_model=InsuranceClaimResponse,
)
def update_insurance_claim(
    claim_id: int,
    claim_update: InsuranceClaimUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return update_insurance_claim_service(
        db=db,
        claim_id=claim_id,
        claim_update=claim_update,
        current_user=current_user,
    )
@router.patch(
    "/{claim_id}/approve",
    response_model=InsuranceClaimResponse,
)
def approve_claim(
    claim_id: int,
    approval: ClaimApprovalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return approve_insurance_claim_service(
        db=db,
        claim_id=claim_id,
        approval=approval,
        current_user=current_user,
    )

@router.delete(
    "/{claim_id}",
)
def delete_insurance_claim(
    claim_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return delete_insurance_claim_service(
        db=db,
        claim_id=claim_id,
        current_user=current_user,
    )