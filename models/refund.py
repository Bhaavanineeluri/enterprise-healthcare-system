from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Refund(BaseModel):

    __tablename__ = "refunds"

    refund_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    payment_id = Column(
        ForeignKey("payments.id"),
        nullable=False,
    )

    refund_amount = Column(
        Numeric(10, 2),
        nullable=False,
    )

    refund_date = Column(
        DateTime,
        nullable=False,
    )

    refund_reason = Column(
        Text,
        nullable=False,
    )

    refund_status = Column(
        String(20),
        default="PENDING",
    )

    remarks = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    payment = relationship(
        "Payment",
        back_populates="refunds",
    )