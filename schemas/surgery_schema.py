from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class SurgeryCreate(BaseModel):

    emr_id: int

    patient_id: int

    doctor_id: int

    surgery_name: str

    surgery_date: date

    operation_theater: Optional[str] = None

    anesthesia_type: Optional[str] = None

    surgeon: Optional[str] = None

    assistant_surgeon: Optional[str] = None

    surgery_notes: Optional[str] = None

    outcome: Optional[str] = None


class SurgeryUpdate(BaseModel):

    surgery_name: Optional[str] = None

    surgery_date: Optional[date] = None

    operation_theater: Optional[str] = None

    anesthesia_type: Optional[str] = None

    surgeon: Optional[str] = None

    assistant_surgeon: Optional[str] = None

    surgery_notes: Optional[str] = None

    outcome: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class SurgeryResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    surgery_code: str

    emr_id: int

    patient_id: int

    doctor_id: int

    surgery_name: str

    surgery_date: date

    operation_theater: Optional[str]

    anesthesia_type: Optional[str]

    surgeon: Optional[str]

    assistant_surgeon: Optional[str]

    surgery_notes: Optional[str]

    outcome: Optional[str]

    status: str

    is_active: bool