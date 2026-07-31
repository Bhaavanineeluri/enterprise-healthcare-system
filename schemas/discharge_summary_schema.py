from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class DischargeSummaryCreate(BaseModel):

    ipd_id: int

    emr_id: int

    patient_id: int

    doctor_id: int

    admission_date: date

    discharge_date: date

    final_diagnosis: str

    procedures_performed: Optional[str] = None

    hospital_course: Optional[str] = None

    condition_at_discharge: Optional[str] = None

    discharge_medications: Optional[str] = None

    follow_up_instructions: Optional[str] = None


class DischargeSummaryUpdate(BaseModel):

    final_diagnosis: Optional[str] = None

    procedures_performed: Optional[str] = None

    hospital_course: Optional[str] = None

    condition_at_discharge: Optional[str] = None

    discharge_medications: Optional[str] = None

    follow_up_instructions: Optional[str] = None

    discharge_status: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class DischargeSummaryResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    discharge_summary_code: str

    ipd_id: int

    emr_id: int

    patient_id: int

    doctor_id: int

    admission_date: date

    discharge_date: date

    final_diagnosis: str

    procedures_performed: Optional[str]

    hospital_course: Optional[str]

    condition_at_discharge: Optional[str]

    discharge_medications: Optional[str]

    follow_up_instructions: Optional[str]

    discharge_status: str

    status: str

    is_active: bool