from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class OPD(BaseModel):

    __tablename__ = "opd"

    opd_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    appointment_id = Column(
        ForeignKey("appointments.id"),
        nullable=False,
        unique=True,
    )

    patient_id = Column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    doctor_id = Column(
        ForeignKey("doctors.id"),
        nullable=False,
    )

    department_id = Column(
        ForeignKey("departments.id"),
        nullable=False,
    )

    visit_datetime = Column(
        DateTime,
        nullable=False,
    )

    token_number = Column(
        Integer,
        nullable=False,
    )

    height = Column(
        Float,
    )

    weight = Column(
        Float,
    )

    bmi = Column(
        Float,
    )

    temperature = Column(
        Float,
    )

    pulse = Column(
        Integer,
    )

    blood_pressure = Column(
        String(20),
    )

    oxygen_saturation = Column(
        Integer,
    )

    status = Column(
        String(30),
        default="WAITING",
    )

    notes = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    appointment = relationship(
        "Appointment",
        back_populates="opd",
    )

    patient = relationship(
        "Patient",
        back_populates="opd_records",
    )

    doctor = relationship(
        "Doctor",
        back_populates="opd_records",
    )

    department = relationship(
        "Department",
        back_populates="opd_records",
    )
    emr_records = relationship(
        "EMR",
        back_populates="opd",
    )