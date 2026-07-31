from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class EMRCreate(BaseModel):

    patient_id: int

    doctor_id: int

    opd_id: Optional[int] = None

    ipd_id: Optional[int] = None

    chief_complaint: Optional[str] = None

    medical_history: Optional[str] = None

    family_history: Optional[str] = None

    allergy_history: Optional[str] = None

    examination: Optional[str] = None

    diagnosis_summary: Optional[str] = None

    treatment_summary: Optional[str] = None


class EMRUpdate(BaseModel):

    chief_complaint: Optional[str] = None

    medical_history: Optional[str] = None

    family_history: Optional[str] = None

    allergy_history: Optional[str] = None

    examination: Optional[str] = None

    diagnosis_summary: Optional[str] = None

    treatment_summary: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class EMRResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    emr_code: str

    patient_id: int

    doctor_id: int

    opd_id: Optional[int]

    ipd_id: Optional[int]

    chief_complaint: Optional[str]

    medical_history: Optional[str]

    family_history: Optional[str]

    allergy_history: Optional[str]

    examination: Optional[str]

    diagnosis_summary: Optional[str]

    treatment_summary: Optional[str]

    status: str

    is_active: bool