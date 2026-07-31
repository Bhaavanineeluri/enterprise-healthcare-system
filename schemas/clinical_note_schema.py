from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class ClinicalNoteCreate(BaseModel):

    emr_id: int

    patient_id: int

    doctor_id: int

    note_type: str

    title: str

    note: str


class ClinicalNoteUpdate(BaseModel):

    note_type: Optional[str] = None

    title: Optional[str] = None

    note: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class ClinicalNoteResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    clinical_note_code: str

    emr_id: int

    patient_id: int

    doctor_id: int

    note_type: str

    title: str

    note: str

    status: str

    is_active: bool