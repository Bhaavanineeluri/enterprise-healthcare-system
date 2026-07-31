from pydantic import BaseModel, ConfigDict, EmailStr

from enum import Enum

class RoleName(str, Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    RECEPTIONIST = "RECEPTIONIST"
    PATIENT = "PATIENT"

class UserRegister(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    password: str
    role_name: RoleName


class LoginResponse(BaseModel):
    message: str
    otp: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    username: str
    email: EmailStr
    role_id: int
    is_active: bool

    model_config = ConfigDict(
        from_attributes=True
    )