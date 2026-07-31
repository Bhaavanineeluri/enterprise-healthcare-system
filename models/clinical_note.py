from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ClinicalNote(BaseModel):

    __tablename__ = "clinical_notes"

    clinical_note_code = Column(
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

    note_type = Column(
        String(50),
        nullable=False,
    )

    title = Column(
        String(255),
        nullable=False,
    )

    note = Column(
        Text,
        nullable=False,
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
        back_populates="clinical_note_records",
    )

    patient = relationship(
        "Patient",
        back_populates="clinical_note_records",
    )

    doctor = relationship(
        "Doctor",
        back_populates="clinical_note_records",
    )