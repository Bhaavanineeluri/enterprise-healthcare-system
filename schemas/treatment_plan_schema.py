from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class TreatmentPlanCreate(BaseModel):

    emr_id: int

    patient_id: int

    doctor_id: int

    treatment_title: str

    treatment_description: Optional[str] = None

    treatment_goals: Optional[str] = None

    follow_up_plan: Optional[str] = None


class TreatmentPlanUpdate(BaseModel):

    treatment_title: Optional[str] = None

    treatment_description: Optional[str] = None

    treatment_goals: Optional[str] = None

    follow_up_plan: Optional[str] = None

    status: Optional[str] = None

    is_active: Optional[bool] = None


class TreatmentPlanResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    treatment_plan_code: str

    emr_id: int

    patient_id: int

    doctor_id: int

    treatment_title: str

    treatment_description: Optional[str]

    treatment_goals: Optional[str]

    follow_up_plan: Optional[str]

    status: str

    is_active: bool