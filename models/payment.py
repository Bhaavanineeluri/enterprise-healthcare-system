from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Payment(BaseModel):

    __tablename__ = "payments"

    payment_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    invoice_id = Column(
        ForeignKey("invoices.id"),
        nullable=False,
    )

    payment_date = Column(
        DateTime,
        nullable=False,
    )

    amount_paid = Column(
        Numeric(10, 2),
        nullable=False,
    )

    payment_method = Column(
        String(30),
        nullable=False,
    )

    payment_status = Column(
        String(30),
        default="SUCCESS",
    )

    transaction_reference = Column(
        String(100),
        unique=True,
    )

    remarks = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    invoice = relationship(
        "Invoice",
        back_populates="payments",
    )

    refunds = relationship(
        "Refund",
        back_populates="payment",
    )
    billing_id = Column(
        ForeignKey("billings.id"),
        nullable=False,
    )

    billing = relationship(
        "Billing",
        back_populates="payments",
    )