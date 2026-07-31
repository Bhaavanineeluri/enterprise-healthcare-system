from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Patient(BaseModel):

    __tablename__ = "patients"

    patient_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    doctor_id = Column(
        ForeignKey("doctors.id"),
        nullable=True
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

    date_of_birth = Column(
        Date,
        nullable=False
    )

    blood_group = Column(
        String(10)
    )

    marital_status = Column(
        String(20)
    )

    phone = Column(
        String(20),
        unique=True,
        nullable=False
    )

    email = Column(
        String(100),
        unique=True
    )

    address = Column(
        Text,
        nullable=False
    )

    city = Column(
        String(100),
        nullable=False
    )

    state = Column(
        String(100),
        nullable=False
    )

    country = Column(
        String(100),
        nullable=False
    )

    postal_code = Column(
        String(20),
        nullable=False
    )

    emergency_contact_name = Column(
        String(100),
        nullable=False
    )

    emergency_contact_number = Column(
        String(20),
        nullable=False
    )

    relationship_with_patient = Column(
        String(50)
    )

    aadhaar_number = Column(
        String(20),
        unique=True
    )

    insurance_provider = Column(
        String(100)
    )

    insurance_policy_number = Column(
        String(100)
    )

    allergies = Column(
        Text
    )

    medical_history = Column(
        Text
    )

    patient_status = Column(
        String(30),
        default="OUTPATIENT"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    doctor = relationship(
        "Doctor",
        back_populates="patients"
    )
    appointments = relationship(
        "Appointment",
        back_populates="patient",
        cascade="all, delete-orphan",
    )
    opd_records = relationship(
        "OPD",
        back_populates="patient",
    )
    ipd_records = relationship(
        "IPD",
        back_populates="patient",
    )
    emr_records = relationship(
        "EMR",
        back_populates="patient",
    )
    diagnosis_records = relationship(
        "Diagnosis",
        back_populates="patient",
    )
    prescription_records = relationship(
        "Prescription",
        back_populates="patient",
    )
    treatment_plan_records = relationship(
        "TreatmentPlan",
        back_populates="patient",
    )
    clinical_note_records = relationship(
        "ClinicalNote",
        back_populates="patient",
    )
    surgery_records = relationship(
        "Surgery",
        back_populates="patient",
    )
    discharge_summaries = relationship(
        "DischargeSummary",
        back_populates="patient",
    )
    lab_orders = relationship(
        "LabOrder",
        back_populates="patient",
    )
    billings = relationship(
        "Billing",
        back_populates="patient",
    )
    documents = relationship(
        "Document",
        back_populates="patient",
    )