from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class BranchCreate(BaseModel):

    hospital_id: int

    branch_name: str

    email: EmailStr

    phone: str

    address: str

    city: str

    state: str

    country: str

    postal_code: str


class BranchUpdate(BaseModel):

    branch_name: Optional[str] = None

    email: Optional[EmailStr] = None

    phone: Optional[str] = None

    address: Optional[str] = None

    city: Optional[str] = None

    state: Optional[str] = None

    country: Optional[str] = None

    postal_code: Optional[str] = None

    is_active: Optional[bool] = None


class BranchResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    branch_code: str

    hospital_id: int

    branch_name: str

    email: EmailStr

    phone: str

    address: str

    city: str

    state: str

    country: str

    postal_code: str

    is_active: bool