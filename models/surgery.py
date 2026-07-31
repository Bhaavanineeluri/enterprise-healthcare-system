from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Surgery(BaseModel):

    __tablename__ = "surgeries"

    surgery_code = Column(
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

    surgery_name = Column(
        String(255),
        nullable=False,
    )

    surgery_date = Column(
        Date,
        nullable=False,
    )

    operation_theater = Column(
        String(100),
    )

    anesthesia_type = Column(
        String(100),
    )

    surgeon = Column(
        String(255),
    )

    assistant_surgeon = Column(
        String(255),
    )

    surgery_notes = Column(
        Text,
    )

    outcome = Column(
        String(100),
    )

    status = Column(
        String(30),
        default="SCHEDULED",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    emr = relationship(
        "EMR",
        back_populates="surgery_records",
    )

    patient = relationship(
        "Patient",
        back_populates="surgery_records",
    )

    doctor = relationship(
        "Doctor",
        back_populates="surgery_records",
    )