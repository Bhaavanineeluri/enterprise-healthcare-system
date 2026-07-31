from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):

    id: int
    full_name: str
    email: EmailStr
    phone: str
    is_active: bool

    class Config:
        from_attributes = True