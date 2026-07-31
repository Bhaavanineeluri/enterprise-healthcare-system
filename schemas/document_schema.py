from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class DocumentCreate(BaseModel):

    patient_id: int

    document_name: str

    document_type: str

    file_path: str

    uploaded_at: datetime

    remarks: Optional[str] = None


class DocumentUpdate(BaseModel):

    document_name: Optional[str] = None

    document_type: Optional[str] = None

    file_path: Optional[str] = None

    remarks: Optional[str] = None

    is_active: Optional[bool] = None


class DocumentResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    patient_id: int

    document_name: str
    document_code: str
    document_type: str

    file_path: str

    uploaded_by: int

    uploaded_at: datetime

    remarks: Optional[str]

    is_active: bool