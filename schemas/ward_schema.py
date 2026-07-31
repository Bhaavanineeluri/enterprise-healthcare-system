from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class WardCreate(BaseModel):

    branch_id: int

    ward_name: str

    ward_type: str

    floor: int

    capacity: int

    incharge_name: Optional[str] = None

    phone: Optional[str] = None

    description: Optional[str] = None


class WardUpdate(BaseModel):

    ward_name: Optional[str] = None

    ward_type: Optional[str] = None

    floor: Optional[int] = None

    capacity: Optional[int] = None

    occupied_beds: Optional[int] = None

    incharge_name: Optional[str] = None

    phone: Optional[str] = None

    description: Optional[str] = None

    is_active: Optional[bool] = None


class WardResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    ward_code: str

    branch_id: int

    ward_name: str

    ward_type: str

    floor: int

    capacity: int

    occupied_beds: int

    incharge_name: Optional[str]

    phone: Optional[str]

    description: Optional[str]

    is_active: bool