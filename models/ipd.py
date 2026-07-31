from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class IPD(BaseModel):

    __tablename__ = "ipd"

    ipd_code = Column(
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

    ward_id = Column(
        ForeignKey("wards.id"),
        nullable=False,
    )

    room_id = Column(
        ForeignKey("rooms.id"),
        nullable=False,
    )

    bed_id = Column(
        ForeignKey("beds.id"),
        nullable=False,
        unique=True,
    )

    admission_date = Column(
        Date,
        nullable=False,
    )

    expected_discharge_date = Column(
        Date,
    )

    actual_discharge_date = Column(
        Date,
    )

    admission_reason = Column(
        Text,
        nullable=False,
    )

    status = Column(
        String(30),
        default="ADMITTED",
    )

    remarks = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    patient = relationship(
        "Patient",
        back_populates="ipd_records",
    )

    doctor = relationship(
        "Doctor",
        back_populates="ipd_records",
    )

    department = relationship(
        "Department",
        back_populates="ipd_records",
    )

    ward = relationship(
        "Ward",
        back_populates="ipd_records",
    )

    room = relationship(
        "Room",
        back_populates="ipd_records",
    )

    bed = relationship(
        "Bed",
        back_populates="ipd_record",
    )
    emr_records = relationship(
        "EMR",
        back_populates="ipd",
    )
    discharge_summaries = relationship(
        "DischargeSummary",
        back_populates="ipd",
    )