from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class EMR(BaseModel):

    __tablename__ = "emr"

    emr_code = Column(
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

    opd_id = Column(
        ForeignKey("opd.id"),
        nullable=True,
    )

    ipd_id = Column(
        ForeignKey("ipd.id"),
        nullable=True,
    )

    chief_complaint = Column(
        Text,
    )

    medical_history = Column(
        Text,
    )

    family_history = Column(
        Text,
    )

    allergy_history = Column(
        Text,
    )

    examination = Column(
        Text,
    )

    diagnosis_summary = Column(
        Text,
    )

    treatment_summary = Column(
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

    patient = relationship(
        "Patient",
        back_populates="emr_records",
    )

    doctor = relationship(
        "Doctor",
        back_populates="emr_records",
    )

    opd = relationship(
        "OPD",
        back_populates="emr_records",
    )

    ipd = relationship(
        "IPD",
        back_populates="emr_records",
    )
    diagnosis_records = relationship(
        "Diagnosis",
        back_populates="emr",
    )
    prescription_records = relationship(
        "Prescription",
        back_populates="emr",
    )
    treatment_plan_records = relationship(
        "TreatmentPlan",
        back_populates="emr",

    )
    clinical_note_records = relationship(
        "ClinicalNote",
        back_populates="emr",
    )
    surgery_records = relationship(
        "Surgery",
        back_populates="emr",
    )
    discharge_summaries = relationship(
        "DischargeSummary",
        back_populates="emr",
    )
    lab_orders = relationship(
        "LabOrder",
        back_populates="emr",
    )