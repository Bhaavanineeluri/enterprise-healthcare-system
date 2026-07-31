from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class BillingCreate(BaseModel):

    patient_id: int

    appointment_id: int

    total_amount: Decimal

    discount: Decimal = Decimal("0.00")

    tax: Decimal = Decimal("0.00")

    billing_date: datetime

    remarks: Optional[str] = None


class BillingUpdate(BaseModel):

    total_amount: Optional[Decimal] = None

    discount: Optional[Decimal] = None

    tax: Optional[Decimal] = None

    billing_date: Optional[datetime] = None

    payment_status: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class BillingResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    billing_code: str

    patient_id: int

    appointment_id: int

    total_amount: Decimal

    discount: Decimal

    tax: Decimal

    net_amount: Decimal

    billing_date: datetime

    payment_status: str

    remarks: Optional[str]

    is_active: bool