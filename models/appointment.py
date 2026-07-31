from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Appointment(BaseModel):

    __tablename__ = "appointments"

    appointment_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
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

    appointment_datetime = Column(
        DateTime,
        nullable=False,
    )

    appointment_type = Column(
        String(30),
        nullable=False,
    )

    status = Column(
        String(30),
        default="SCHEDULED",
    )

    chief_complaint = Column(
        Text,
    )

    notes = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    patient = relationship(
        "Patient",
        back_populates="appointments",
    )

    doctor = relationship(
        "Doctor",
        back_populates="appointments",
    )

    department = relationship(
        "Department",
        back_populates="appointments",
    )
    opd = relationship(
        "OPD",
        back_populates="appointment",
        uselist=False,
    )
    billings = relationship(
        "Billing",
        back_populates="appointment",
    )