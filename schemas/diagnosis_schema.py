from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class DiagnosisCreate(BaseModel):

    emr_id: int

    patient_id: int

    doctor_id: int

    diagnosis_name: str

    diagnosis_type: str

    icd10_code: Optional[str] = None

    description: Optional[str] = None


class DiagnosisUpdate(BaseModel):

    diagnosis_name: Optional[str] = None

    diagnosis_type: Optional[str] = None

    icd10_code: Optional[str] = None

    description: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class DiagnosisResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    diagnosis_code: str

    emr_id: int

    patient_id: int

    doctor_id: int

    diagnosis_name: str

    diagnosis_type: str

    icd10_code: Optional[str]

    description: Optional[str]

    status: str

    is_active: bool