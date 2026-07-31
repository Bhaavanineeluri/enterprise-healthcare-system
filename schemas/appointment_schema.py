from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class AppointmentCreate(BaseModel):

    patient_id: int

    doctor_id: int

    department_id: int

    appointment_datetime: datetime

    appointment_type: str

    chief_complaint: Optional[str] = None

    notes: Optional[str] = None


class AppointmentUpdate(BaseModel):

    doctor_id: Optional[int] = None

    department_id: Optional[int] = None

    appointment_datetime: Optional[datetime] = None

    appointment_type: Optional[str] = None

    status: Optional[str] = None

    chief_complaint: Optional[str] = None

    notes: Optional[str] = None

    is_active: Optional[bool] = None


class AppointmentResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    appointment_code: str

    patient_id: int

    doctor_id: int

    department_id: int

    appointment_datetime: datetime

    appointment_type: str

    status: str

    chief_complaint: Optional[str]

    notes: Optional[str]

    is_active: bool