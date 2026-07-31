from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class PrescriptionCreate(BaseModel):

    emr_id: int

    patient_id: int

    doctor_id: int

    medicine_name: str

    dosage: str

    frequency: str

    duration: str

    instructions: Optional[str] = None


class PrescriptionUpdate(BaseModel):

    medicine_name: Optional[str] = None

    dosage: Optional[str] = None

    frequency: Optional[str] = None

    duration: Optional[str] = None

    instructions: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class PrescriptionResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    prescription_code: str

    emr_id: int

    patient_id: int

    doctor_id: int

    medicine_name: str

    dosage: str

    frequency: str

    duration: str

    instructions: Optional[str]

    status: str

    is_active: bool