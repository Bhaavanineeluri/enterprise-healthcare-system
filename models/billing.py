from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Billing(BaseModel):

    __tablename__ = "billings"

    billing_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    patient_id = Column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    appointment_id = Column(
        ForeignKey("appointments.id"),
        nullable=False,
    )

    total_amount = Column(
        Numeric(10, 2),
        nullable=False,
    )

    discount = Column(
        Numeric(10, 2),
        default=0,
    )

    tax = Column(
        Numeric(10, 2),
        default=0,
    )

    net_amount = Column(
        Numeric(10, 2),
        nullable=False,
    )

    billing_date = Column(
        DateTime,
        nullable=False,
    )

    payment_status = Column(
        String(30),
        default="PENDING",
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
        back_populates="billings",
    )

    appointment = relationship(
        "Appointment",
        back_populates="billings",
    )

    invoices = relationship(
        "Invoice",
        back_populates="billing",
    )

    payments = relationship(
        "Payment",
        back_populates="billing",
    )
    insurance_claims = relationship(
        "InsuranceClaim",
        back_populates="billing",
    )