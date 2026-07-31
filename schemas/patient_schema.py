from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr


class PatientCreate(BaseModel):

    doctor_id: Optional[int] = None

    first_name: str

    last_name: str

    gender: str

    date_of_birth: date

    blood_group: Optional[str] = None

    marital_status: Optional[str] = None

    phone: str

    email: Optional[EmailStr] = None

    address: str

    city: str

    state: str

    country: str

    postal_code: str

    emergency_contact_name: str

    emergency_contact_number: str

    relationship_with_patient: Optional[str] = None

    aadhaar_number: Optional[str] = None

    insurance_provider: Optional[str] = None

    insurance_policy_number: Optional[str] = None

    allergies: Optional[str] = None

    medical_history: Optional[str] = None


class PatientUpdate(BaseModel):

    doctor_id: Optional[int] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    gender: Optional[str] = None

    date_of_birth: Optional[date] = None

    blood_group: Optional[str] = None

    marital_status: Optional[str] = None

    phone: Optional[str] = None

    email: Optional[EmailStr] = None

    address: Optional[str] = None

    city: Optional[str] = None

    state: Optional[str] = None

    country: Optional[str] = None

    postal_code: Optional[str] = None

    emergency_contact_name: Optional[str] = None

    emergency_contact_number: Optional[str] = None

    relationship_with_patient: Optional[str] = None

    aadhaar_number: Optional[str] = None

    insurance_provider: Optional[str] = None

    insurance_policy_number: Optional[str] = None

    allergies: Optional[str] = None

    medical_history: Optional[str] = None

    patient_status: Optional[str] = None

    is_active: Optional[bool] = None


class PatientResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    patient_code: str

    doctor_id: Optional[int]

    first_name: str

    last_name: str

    gender: str

    date_of_birth: date

    blood_group: Optional[str]

    marital_status: Optional[str]

    phone: str

    email: Optional[EmailStr]

    address: str

    city: str

    state: str

    country: str

    postal_code: str

    emergency_contact_name: str

    emergency_contact_number: str

    relationship_with_patient: Optional[str]

    aadhaar_number: Optional[str]

    insurance_provider: Optional[str]

    insurance_policy_number: Optional[str]

    allergies: Optional[str]

    medical_history: Optional[str]

    patient_status: str

    is_active: bool