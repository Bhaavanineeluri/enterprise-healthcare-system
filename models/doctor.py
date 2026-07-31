from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Doctor(BaseModel):

    __tablename__ = "doctors"

    doctor_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    department_id = Column(
        ForeignKey("departments.id"),
        nullable=False
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    gender = Column(
        String(20),
        nullable=False
    )

    specialization = Column(
        String(100),
        nullable=False
    )

    qualification = Column(
        String(150),
        nullable=False
    )

    license_number = Column(
        String(100),
        unique=True,
        nullable=False
    )

    experience = Column(
        Integer,
        default=0
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=False
    )

    consultation_fee = Column(
        Numeric(10, 2),
        default=0
    )

    status = Column(
        String(30),
        default="Available"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    department = relationship(
        "Department",
        back_populates="doctors"
    )
    patients = relationship(
        "Patient",
        back_populates="doctor",
        cascade="all, delete-orphan"
    )
    appointments = relationship(
        "Appointment",
        back_populates="doctor",
    )
    opd_records = relationship(
        "OPD",
        back_populates="doctor",
    )
    ipd_records = relationship(
        "IPD",
        back_populates="doctor",
    )
    emr_records = relationship(
        "EMR",
        back_populates="doctor",
    )
    diagnosis_records = relationship(
        "Diagnosis",
        back_populates="doctor",
    )
    prescription_records = relationship(
        "Prescription",
        back_populates="doctor",
    )
    treatment_plan_records = relationship(
        "TreatmentPlan",
        back_populates="doctor",
    )
    clinical_note_records = relationship(
        "ClinicalNote",
        back_populates="doctor",
    )
    surgery_records = relationship(
        "Surgery",
        back_populates="doctor",
    )
    discharge_summaries = relationship(
        "DischargeSummary",
        back_populates="doctor",
    )
    lab_orders = relationship(
        "LabOrder",
        back_populates="doctor",
    )
            