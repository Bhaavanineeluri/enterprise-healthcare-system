from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class BedCreate(BaseModel):

    room_id: int

    bed_number: str

    bed_type: str


class BedUpdate(BaseModel):

    room_id: Optional[int] = None

    bed_number: Optional[str] = None

    bed_type: Optional[str] = None

    bed_status: Optional[str] = None

    patient_id: Optional[int] = None

    is_active: Optional[bool] = None


class BedResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    bed_code: str

    room_id: int

    patient_id: Optional[int]

    bed_number: str

    bed_type: str

    bed_status: str

    is_active: bool