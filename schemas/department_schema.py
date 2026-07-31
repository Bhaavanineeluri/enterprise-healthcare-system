from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class DepartmentCreate(BaseModel):

    branch_id: int

    department_name: str

    description: Optional[str] = None

    phone: Optional[str] = None

    email: Optional[EmailStr] = None

    location: Optional[str] = None


class DepartmentUpdate(BaseModel):

    department_name: Optional[str] = None

    description: Optional[str] = None

    phone: Optional[str] = None

    email: Optional[EmailStr] = None

    location: Optional[str] = None

    is_active: Optional[bool] = None


class DepartmentResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    department_code: str

    branch_id: int

    department_name: str

    description: Optional[str]

    phone: Optional[str]

    email: Optional[EmailStr]

    location: Optional[str]

    is_active: bool