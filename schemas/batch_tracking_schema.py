from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class BatchTrackingCreate(BaseModel):

    pharmacy_inventory_id: int

    manufacturing_date: date

    recall_status: str = "NOT_RECALLED"

    manufacturer: str

    remarks: Optional[str] = None


class BatchTrackingUpdate(BaseModel):

    manufacturing_date: Optional[date] = None

    recall_status: Optional[str] = None

    manufacturer: Optional[str] = None

    remarks: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class BatchTrackingResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    batch_tracking_code: str

    pharmacy_inventory_id: int

    manufacturing_date: date

    recall_status: str

    manufacturer: str

    remarks: Optional[str]

    status: str

    is_active: bool