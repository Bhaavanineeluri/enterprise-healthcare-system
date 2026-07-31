from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class StaffCreate(BaseModel):

    department_id: int

    first_name: str

    last_name: str

    gender: str

    designation: str

    employee_type: str

    qualification: Optional[str] = None

    email: EmailStr

    phone: str

    joining_date: str


class StaffUpdate(BaseModel):

    department_id: Optional[int] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    gender: Optional[str] = None

    designation: Optional[str] = None

    employee_type: Optional[str] = None

    qualification: Optional[str] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = None

    joining_date: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class StaffResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    staff_code: str

    department_id: int

    first_name: str

    last_name: str

    gender: str

    designation: str

    employee_type: str

    qualification: Optional[str]

    email: EmailStr

    phone: str

    joining_date: str

    status: str

    is_active: bool