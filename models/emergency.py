from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Emergency(BaseModel):

    __tablename__ = "emergencies"

    emergency_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    patient_id = Column(
        ForeignKey("patients.id"),
        nullable=False
    )

    doctor_id = Column(
        ForeignKey("doctors.id"),
        nullable=True
    )

    emergency_type = Column(
        String(100),
        nullable=False
    )

    priority = Column(
        String(20),
        nullable=False
    )

    arrival_time = Column(
        DateTime,
        nullable=False
    )

    symptoms = Column(
        Text,
        nullable=False
    )

    diagnosis = Column(
        Text
    )

    treatment = Column(
        Text
    )

    status = Column(
        String(30),
        default="OPEN"
    )

    remarks = Column(
        Text
    )

    is_active = Column(
        Boolean,
        default=True
    )

    patient = relationship(
        "Patient"
    )

    doctor = relationship(
        "Doctor"
    )