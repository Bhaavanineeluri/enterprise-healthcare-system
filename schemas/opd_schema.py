from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class OPDCreate(BaseModel):

    appointment_id: int

    patient_id: int

    doctor_id: int

    department_id: int

    visit_datetime: datetime

    token_number: int

    height: Optional[float] = None

    weight: Optional[float] = None

    bmi: Optional[float] = None

    temperature: Optional[float] = None

    pulse: Optional[int] = None

    blood_pressure: Optional[str] = None

    oxygen_saturation: Optional[int] = None

    notes: Optional[str] = None


class OPDUpdate(BaseModel):

    height: Optional[float] = None

    weight: Optional[float] = None

    bmi: Optional[float] = None

    temperature: Optional[float] = None

    pulse: Optional[int] = None

    blood_pressure: Optional[str] = None

    oxygen_saturation: Optional[int] = None

    notes: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class OPDResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    opd_code: str

    appointment_id: int

    patient_id: int

    doctor_id: int

    department_id: int

    visit_datetime: datetime

    

    height: Optional[float]

    weight: Optional[float]

    bmi: Optional[float]

    temperature: Optional[float]

    pulse: Optional[int]

    blood_pressure: Optional[str]

    oxygen_saturation: Optional[int]

    status: str

    notes: Optional[str]

    is_active: bool