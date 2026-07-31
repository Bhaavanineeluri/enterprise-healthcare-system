from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class RoomCreate(BaseModel):

    ward_id: int

    room_number: str

    room_type: str

    floor: int

    total_beds: int


class RoomUpdate(BaseModel):

    ward_id: Optional[int] = None

    room_number: Optional[str] = None

    room_type: Optional[str] = None

    floor: Optional[int] = None

    total_beds: Optional[int] = None

    occupied_beds: Optional[int] = None

    room_status: Optional[str] = None

    is_active: Optional[bool] = None


class RoomResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    room_code: str

    ward_id: int

    room_number: str

    room_type: str

    floor: int

    total_beds: int

    occupied_beds: int

    room_status: str

    is_active: bool