from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class TestProcessingCreate(BaseModel):

    lab_order_id: int

    processed_by: str

    processing_start: datetime

    processing_end: Optional[datetime] = None

    observations: Optional[str] = None

    remarks: Optional[str] = None


class TestProcessingUpdate(BaseModel):

    processed_by: Optional[str] = None

    processing_start: Optional[datetime] = None

    processing_end: Optional[datetime] = None

    observations: Optional[str] = None

    remarks: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class TestProcessingResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    processing_code: str

    lab_order_id: int

    processed_by: str

    processing_start: datetime

    processing_end: Optional[datetime]

    observations: Optional[str]

    remarks: Optional[str]

    status: str

    is_active: bool