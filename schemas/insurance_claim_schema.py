from datetime import date
from decimal import Decimal
from typing import Optional
from typing import Literal
from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import BaseModel
from pydantic import ConfigDict


class InsuranceClaimCreate(BaseModel):

    billing_id: int

    insurance_provider: str

    policy_number: str

    claim_amount: Decimal

    claim_date: date

    remarks: Optional[str] = None
    
    approved_by: Optional[int] = None

    approval_date: Optional[datetime] = None

class InsuranceClaimUpdate(BaseModel):

    insurance_provider: Optional[str] = None

    policy_number: Optional[str] = None

    claim_amount: Optional[Decimal] = None

    claim_status: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class InsuranceClaimResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    claim_code: str

    billing_id: int

    insurance_provider: str

    policy_number: str

    claim_amount: Decimal

    claim_date: date

    claim_status: str

    remarks: Optional[str]

    is_active: bool
    
    approved_by: Optional[int]

    approval_date: Optional[datetime]


class ClaimApprovalRequest(BaseModel):

    approval_status: Literal[
        "APPROVED",
        "REJECTED",
    ]

    remarks: Optional[str] = None