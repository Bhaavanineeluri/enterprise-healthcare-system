from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class PrescriptionValidationCreate(BaseModel):

    prescription_id: int

    pharmacy_inventory_id: int

    requested_quantity: int

    approved_quantity: int

    remarks: Optional[str] = None

    validated_by: str

    validation_date: datetime


class PrescriptionValidationUpdate(BaseModel):

    requested_quantity: Optional[int] = None

    approved_quantity: Optional[int] = None

    validation_status: Optional[str] = None

    remarks: Optional[str] = None

    validated_by: Optional[str] = None

    validation_date: Optional[datetime] = None

    is_active: Optional[bool] = None


class PrescriptionValidationResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    validation_code: str

    prescription_id: int

    pharmacy_inventory_id: int

    requested_quantity: int

    approved_quantity: int

    validation_status: str

    remarks: Optional[str]

    validated_by: str

    validation_date: datetime

    is_active: bool