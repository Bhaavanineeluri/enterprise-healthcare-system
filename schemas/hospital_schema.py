from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class HospitalCreate(BaseModel):

    hospital_name: str

    registration_number: str

    license_number: str

    hospital_type: str

    email: EmailStr

    phone: str

    website: Optional[str] = None

    address: str

    city: str

    state: str

    country: str

    postal_code: str

    timezone: str

    description: Optional[str] = None


class HospitalUpdate(BaseModel):

    hospital_name: Optional[str] = None

    registration_number: Optional[str] = None

    license_number: Optional[str] = None

    hospital_type: Optional[str] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = None

    website: Optional[str] = None

    address: Optional[str] = None

    city: Optional[str] = None

    state: Optional[str] = None

    country: Optional[str] = None

    postal_code: Optional[str] = None

    timezone: Optional[str] = None

    description: Optional[str] = None

    is_active: Optional[bool] = None


class HospitalResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    hospital_code: str

    hospital_name: str

    registration_number: str

    license_number: str

    hospital_type: str

    email: EmailStr

    phone: str

    website: Optional[str]

    address: str

    city: str

    state: str

    country: str

    postal_code: str

    timezone: str

    description: Optional[str]

    is_active: bool