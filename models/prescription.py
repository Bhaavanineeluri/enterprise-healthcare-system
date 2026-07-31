from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Prescription(BaseModel):

    __tablename__ = "prescriptions"

    prescription_code = Column(
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

    medicine_name = Column(
        String(255),
        nullable=False,
    )

    dosage = Column(
        String(100),
        nullable=False,
    )

    frequency = Column(
        String(100),
        nullable=False,
    )

    duration = Column(
        String(100),
        nullable=False,
    )

    instructions = Column(
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
        back_populates="prescription_records",
    )

    patient = relationship(
        "Patient",
        back_populates="prescription_records",
    )

    doctor = relationship(
        "Doctor",
        back_populates="prescription_records",
    )
    prescription_validations = relationship(
        "PrescriptionValidation",
        back_populates="prescription",
    )