from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class AmbulanceCreate(BaseModel):

    vehicle_number: str

    vehicle_type: str

    driver_name: str

    driver_phone: str

    current_location: Optional[str] = None


class AmbulanceUpdate(BaseModel):

    vehicle_number: Optional[str] = None

    vehicle_type: Optional[str] = None

    driver_name: Optional[str] = None

    driver_phone: Optional[str] = None

    current_location: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class AmbulanceResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    ambulance_code: str

    vehicle_number: str

    vehicle_type: str

    driver_name: str

    driver_phone: str

    current_location: Optional[str]

    status: str

    is_active: bool