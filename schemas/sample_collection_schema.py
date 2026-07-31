from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class SampleCollectionCreate(BaseModel):

    lab_order_id: int

    sample_type: str

    sample_container: Optional[str] = None

    collected_by: str

    collection_datetime: datetime

    remarks: Optional[str] = None


class SampleCollectionUpdate(BaseModel):

    sample_type: Optional[str] = None

    sample_container: Optional[str] = None

    collected_by: Optional[str] = None

    collection_datetime: Optional[datetime] = None

    remarks: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class SampleCollectionResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    sample_collection_code: str

    lab_order_id: int

    sample_type: str

    sample_container: Optional[str]

    collected_by: str

    collection_datetime: datetime

    remarks: Optional[str]

    status: str

    is_active: bool