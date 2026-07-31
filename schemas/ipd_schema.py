from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class IPDCreate(BaseModel):

    patient_id: int

    doctor_id: int

    department_id: int

    ward_id: int

    room_id: int

    bed_id: int

    admission_date: date

    expected_discharge_date: Optional[date] = None

    admission_reason: str

    remarks: Optional[str] = None


class IPDUpdate(BaseModel):

    doctor_id: Optional[int] = None

    department_id: Optional[int] = None

    ward_id: Optional[int] = None

    room_id: Optional[int] = None

    bed_id: Optional[int] = None

    expected_discharge_date: Optional[date] = None

    actual_discharge_date: Optional[date] = None

    admission_reason: Optional[str] = None

    status: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class IPDResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    ipd_code: str

    patient_id: int

    doctor_id: int

    department_id: int

    ward_id: int

    room_id: int

    bed_id: int

    admission_date: date

    expected_discharge_date: Optional[date]

    actual_discharge_date: Optional[date]

    admission_reason: str

    status: str

    remarks: Optional[str]

    is_active: bool