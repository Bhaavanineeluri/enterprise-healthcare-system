from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class ExpiryManagementCreate(BaseModel):

    pharmacy_inventory_id: int

    review_date: date

    reviewed_by: str

    remarks: Optional[str] = None


class ExpiryManagementUpdate(BaseModel):

    review_date: Optional[date] = None

    reviewed_by: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class ExpiryManagementResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    expiry_code: str

    pharmacy_inventory_id: int

    review_date: date

    expiry_status: str

    reviewed_by: str

    remarks: Optional[str]

    is_active: bool