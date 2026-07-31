from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class LabOrder(BaseModel):

    __tablename__ = "lab_orders"

    lab_order_code = Column(
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

    test_name = Column(
        String(255),
        nullable=False,
    )

    test_category = Column(
        String(100),
        nullable=False,
    )

    priority = Column(
        String(30),
        default="NORMAL",
    )

    clinical_notes = Column(
        Text,
    )

    order_date = Column(
        Date,
        nullable=False,
    )

    status = Column(
        String(30),
        default="ORDERED",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    emr = relationship(
        "EMR",
        back_populates="lab_orders",
    )

    patient = relationship(
        "Patient",
        back_populates="lab_orders",
    )

    doctor = relationship(
        "Doctor",
        back_populates="lab_orders",
    )
    sample_collections = relationship(
        "SampleCollection",
        back_populates="lab_order",
    )
    test_processing = relationship(
        "TestProcessing",
        back_populates="lab_order",
        uselist=False,
    )
    result_publishing = relationship(
        "ResultPublishing",
        back_populates="lab_order",
        uselist=False,
    )