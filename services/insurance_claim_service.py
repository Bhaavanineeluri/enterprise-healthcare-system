from sqlalchemy.orm import Session

from core.exceptions import (
    bad_request,
    not_found,
)
from datetime import datetime

from models.insurance_claim import InsuranceClaim
from models.user import User

from repositories.billing_repository import (
    get_billing_by_id,
)
from schemas.insurance_claim_schema import (
    ClaimApprovalRequest,
)
from repositories.insurance_claim_repository import (
    create_insurance_claim,
    delete_insurance_claim,
    get_all_insurance_claims,
    get_insurance_claim_by_id,
    get_insurance_claim_count,
    update_insurance_claim,
)

from schemas.insurance_claim_schema import (
    InsuranceClaimCreate,
    InsuranceClaimUpdate,
    ClaimApprovalRequest
)

from services.audit_service import (
    save_audit_log,
)


VALID_CLAIM_STATUS = {
    "PENDING",
    "APPROVED",
    "REJECTED",
}


def generate_claim_code(
    db: Session,
):

    count = get_insurance_claim_count(db)

    return f"CLAIM{count + 1:06d}"


def create_insurance_claim_service(
    db: Session,
    claim: InsuranceClaimCreate,
    current_user: User,
):

    billing = get_billing_by_id(
        db,
        claim.billing_id,
    )

    if billing is None:

        not_found(
            "Billing record not found."
        )

    if claim.claim_amount <= 0:

        bad_request(
            "Claim amount must be greater than zero."
        )

    if claim.claim_amount > billing.net_amount:

        bad_request(
            "Claim amount cannot exceed billing amount."
        )

    new_claim = InsuranceClaim(

        claim_code=generate_claim_code(
            db,
        ),

        billing_id=claim.billing_id,

        insurance_provider=claim.insurance_provider,

        policy_number=claim.policy_number,

        claim_amount=claim.claim_amount,

        claim_date=claim.claim_date,

        claim_status="PENDING",

        remarks=claim.remarks,
    )

    created = create_insurance_claim(
        db,
        new_claim,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="INSURANCE_CLAIM",
        action="CREATE",
    )

    return created


def get_all_insurance_claims_service(
    db: Session,
    current_user: User,
):

    return get_all_insurance_claims(
        db,
    )




def approve_insurance_claim_service(
    db: Session,
    claim_id: int,
    approval: ClaimApprovalRequest,
    current_user: User,
):

    claim = get_insurance_claim_by_id(
        db,
        claim_id,
    )

    if claim is None:

        not_found(
            "Insurance claim not found."
        )

    claim.claim_status = approval.approval_status

    claim.approved_by = current_user.id

    claim.approval_date = datetime.utcnow()

    claim.remarks = approval.remarks

    updated_claim = update_insurance_claim(
        db,
        claim,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="INSURANCE_CLAIM",
        action="APPROVE",
    )

    return updated_claim
def get_insurance_claim_service(
    db: Session,
    claim_id: int,
    current_user: User,
):

    claim = get_insurance_claim_by_id(
        db,
        claim_id,
    )

    if claim is None:

        not_found(
            "Insurance claim not found."
        )

    return claim


def update_insurance_claim_service(
    db: Session,
    claim_id: int,
    claim_update: InsuranceClaimUpdate,
    current_user: User,
):

    claim = get_insurance_claim_by_id(
        db,
        claim_id,
    )

    if claim is None:

        not_found(
            "Insurance claim not found."
        )

    update_data = claim_update.model_dump(
        exclude_unset=True,
    )

    if (
        "claim_status" in update_data
        and update_data["claim_status"] not in VALID_CLAIM_STATUS
    ):

        bad_request(
            "Invalid claim status."
        )

    for key, value in update_data.items():

        setattr(
            claim,
            key,
            value,
        )

    updated = update_insurance_claim(
        db,
        claim,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="INSURANCE_CLAIM",
        action="UPDATE",
    )

    return updated


def delete_insurance_claim_service(
    db: Session,
    claim_id: int,
    current_user: User,
):

    claim = get_insurance_claim_by_id(
        db,
        claim_id,
    )

    if claim is None:

        not_found(
            "Insurance claim not found."
        )

    delete_insurance_claim(
        db,
        claim,
    )

    save_audit_log(
        db=db,
        current_user=current_user,
        module="INSURANCE_CLAIM",
        action="DELETE",
    )

    return {
        "message": "Insurance claim deleted successfully."
    }