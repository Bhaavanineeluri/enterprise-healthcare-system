from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Invoice(BaseModel):

    __tablename__ = "invoices"

    invoice_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    billing_id = Column(
        ForeignKey("billings.id"),
        nullable=False,
    )

    invoice_date = Column(
        DateTime,
        nullable=False,
    )

    due_date = Column(
        DateTime,
        nullable=False,
    )

    invoice_amount = Column(
        Numeric(10, 2),
        nullable=False,
    )

    invoice_status = Column(
        String(30),
        default="UNPAID",
    )

    remarks = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    billing = relationship(
        "Billing",
        back_populates="invoices",
    )

    payments = relationship(
        "Payment",
        back_populates="invoice",
    )