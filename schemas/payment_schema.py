from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class PaymentCreate(BaseModel):

    invoice_id: int

    payment_date: datetime

    amount_paid: Decimal

    payment_method: str

    transaction_reference: Optional[str] = None

    remarks: Optional[str] = None
    billing_id: int


class PaymentUpdate(BaseModel):

    payment_method: Optional[str] = None

    payment_status: Optional[str] = None

    transaction_reference: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class PaymentResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    payment_code: str

    invoice_id: int

    payment_date: datetime

    amount_paid: Decimal

    payment_method: str

    payment_status: str

    transaction_reference: Optional[str]

    remarks: Optional[str]

    is_active: bool