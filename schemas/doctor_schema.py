from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class DoctorCreate(BaseModel):

    department_id: int

    first_name: str

    last_name: str

    gender: str

    specialization: str

    qualification: str

    license_number: str

    experience: int

    email: EmailStr

    phone: str

    consultation_fee: Decimal


class DoctorUpdate(BaseModel):

    department_id: Optional[int] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    gender: Optional[str] = None

    specialization: Optional[str] = None

    qualification: Optional[str] = None

    license_number: Optional[str] = None

    experience: Optional[int] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = None

    consultation_fee: Optional[Decimal] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class DoctorResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    doctor_code: str

    department_id: int

    first_name: str

    last_name: str

    gender: str

    specialization: str

    qualification: str

    license_number: str

    experience: int

    email: EmailStr

    phone: str

    consultation_fee: Decimal

    status: str

    is_active: bool