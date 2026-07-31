from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class InsuranceClaim(BaseModel):

    __tablename__ = "insurance_claims"

    claim_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    billing_id = Column(
        ForeignKey("billings.id"),
        nullable=False,
    )

    insurance_provider = Column(
        String(150),
        nullable=False,
    )

    policy_number = Column(
        String(100),
        nullable=False,
    )

    claim_amount = Column(
        Numeric(10, 2),
        nullable=False,
    )

    claim_date = Column(
        Date,
        nullable=False,
    )

    claim_status = Column(
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
    approved_by = Column(
        ForeignKey("users.id"),
        nullable=True,
    )

    approval_date = Column(
        DateTime,
        nullable=True,
    )

    approver = relationship(
        "User",
    )
    billing = relationship(
        "Billing",
        back_populates="insurance_claims",
    )