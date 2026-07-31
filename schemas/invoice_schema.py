from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class InvoiceCreate(BaseModel):

    billing_id: int

    invoice_date: datetime

    due_date: datetime

    remarks: Optional[str] = None


class InvoiceUpdate(BaseModel):

    due_date: Optional[datetime] = None

    invoice_status: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class InvoiceResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    invoice_code: str

    billing_id: int

    invoice_date: datetime

    due_date: datetime

    invoice_amount: Decimal

    invoice_status: str

    remarks: Optional[str]

    is_active: bool