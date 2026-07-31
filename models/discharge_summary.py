from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class DischargeSummary(BaseModel):

    __tablename__ = "discharge_summaries"

    discharge_summary_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    ipd_id = Column(
        ForeignKey("ipd.id"),
        nullable=False,
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

    admission_date = Column(
        Date,
        nullable=False,
    )

    discharge_date = Column(
        Date,
        nullable=False,
    )

    final_diagnosis = Column(
        Text,
        nullable=False,
    )

    procedures_performed = Column(
        Text,
    )

    hospital_course = Column(
        Text,
    )

    condition_at_discharge = Column(
        Text,
    )

    discharge_medications = Column(
        Text,
    )

    follow_up_instructions = Column(
        Text,
    )

    discharge_status = Column(
        String(50),
        default="DISCHARGED",
    )

    status = Column(
        String(30),
        default="ACTIVE",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    ipd = relationship(
        "IPD",
        back_populates="discharge_summaries",
    )

    emr = relationship(
        "EMR",
        back_populates="discharge_summaries",
    )

    patient = relationship(
        "Patient",
        back_populates="discharge_summaries",
    )

    doctor = relationship(
        "Doctor",
        back_populates="discharge_summaries",
    )