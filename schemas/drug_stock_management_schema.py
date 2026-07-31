from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class DrugStockManagementCreate(BaseModel):

    pharmacy_inventory_id: int

    transaction_type: str

    quantity: int

    remarks: Optional[str] = None

    updated_by: str

    updated_at: datetime


class DrugStockManagementUpdate(BaseModel):

    transaction_type: Optional[str] = None

    quantity: Optional[int] = None

    remarks: Optional[str] = None

    updated_by: Optional[str] = None

    updated_at: Optional[datetime] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class DrugStockManagementResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    stock_code: str

    pharmacy_inventory_id: int

    transaction_type: str

    quantity: int

    previous_quantity: int

    updated_quantity: int

    remarks: Optional[str]

    updated_by: str

    updated_at: datetime

    status: str

    is_active: bool