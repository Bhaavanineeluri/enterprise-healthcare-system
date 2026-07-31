from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class EmergencyCreate(BaseModel):

    patient_id: int

    doctor_id: Optional[int] = None

    emergency_type: str

    priority: str

    arrival_time: datetime

    symptoms: str

    diagnosis: Optional[str] = None

    treatment: Optional[str] = None

    remarks: Optional[str] = None


class EmergencyUpdate(BaseModel):

    doctor_id: Optional[int] = None

    emergency_type: Optional[str] = None

    priority: Optional[str] = None

    diagnosis: Optional[str] = None

    treatment: Optional[str] = None

    status: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class EmergencyResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    emergency_code: str

    patient_id: int

    doctor_id: Optional[int]

    emergency_type: str

    priority: str

    arrival_time: datetime

    symptoms: str

    diagnosis: Optional[str]

    treatment: Optional[str]

    status: str

    remarks: Optional[str]

    is_active: bool