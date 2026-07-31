from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class RefundCreate(BaseModel):

    payment_id: int

    refund_amount: Decimal

    refund_date: datetime

    refund_reason: str

    remarks: Optional[str] = None


class RefundUpdate(BaseModel):

    refund_status: Optional[str] = None

    refund_reason: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class RefundResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    refund_code: str

    payment_id: int

    refund_amount: Decimal

    refund_date: datetime

    refund_reason: str

    refund_status: str

    remarks: Optional[str]

    is_active: bool