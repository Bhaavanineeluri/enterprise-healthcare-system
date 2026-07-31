from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class MedicineDispensingCreate(BaseModel):

    prescription_validation_id: int

    pharmacy_inventory_id: int

    dispensed_quantity: int

    dispensed_by: str

    dispensed_at: datetime

    remarks: Optional[str] = None


class MedicineDispensingUpdate(BaseModel):

    dispensed_quantity: Optional[int] = None

    dispensed_by: Optional[str] = None

    dispensed_at: Optional[datetime] = None

    remarks: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class MedicineDispensingResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    dispensing_code: str

    prescription_validation_id: int

    pharmacy_inventory_id: int

    dispensed_quantity: int

    dispensed_by: str

    dispensed_at: datetime

    remarks: Optional[str]

    status: str

    is_active: bool