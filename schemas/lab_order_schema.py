from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class LabOrderCreate(BaseModel):

    emr_id: int

    patient_id: int

    doctor_id: int

    test_name: str

    test_category: str

    priority: str = "NORMAL"

    clinical_notes: Optional[str] = None

    order_date: date


class LabOrderUpdate(BaseModel):

    test_name: Optional[str] = None

    test_category: Optional[str] = None

    priority: Optional[str] = None

    clinical_notes: Optional[str] = None

    order_date: Optional[date] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class LabOrderResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    lab_order_code: str

    emr_id: int

    patient_id: int

    doctor_id: int

    test_name: str

    test_category: str

    priority: str

    clinical_notes: Optional[str]

    order_date: date

    status: str

    is_active: bool