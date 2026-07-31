from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class TreatmentPlan(BaseModel):

    __tablename__ = "treatment_plans"

    treatment_plan_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    emr_id = Column(
        ForeignKey("emr.id"),
        nullable=False,
    )

    patient_id = Column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    doctor_id = Column(
        ForeignKey("doctors.id"),
        nullable=False,
    )

    treatment_title = Column(
        String(255),
        nullable=False,
    )

    treatment_description = Column(
        Text,
    )

    treatment_goals = Column(
        Text,
    )

    follow_up_plan = Column(
        Text,
    )

    status = Column(
        String(30),
        default="ACTIVE",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    emr = relationship(
        "EMR",
        back_populates="treatment_plan_records",
    )

    patient = relationship(
        "Patient",
        back_populates="treatment_plan_records",
    )

    doctor = relationship(
        "Doctor",
        back_populates="treatment_plan_records",
    )