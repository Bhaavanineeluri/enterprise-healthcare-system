from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class ResultPublishingCreate(BaseModel):

    lab_order_id: int

    result: str

    reference_range: Optional[str] = None

    interpretation: Optional[str] = None

    approved_by: str

    published_at: datetime


class ResultPublishingUpdate(BaseModel):

    result: Optional[str] = None

    reference_range: Optional[str] = None

    interpretation: Optional[str] = None

    approved_by: Optional[str] = None

    published_at: Optional[datetime] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class ResultPublishingResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    result_code: str

    lab_order_id: int

    result: str

    reference_range: Optional[str]

    interpretation: Optional[str]

    approved_by: str

    published_at: datetime

    status: str

    is_active: bool