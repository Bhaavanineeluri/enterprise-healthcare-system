from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ResultPublishing(BaseModel):

    __tablename__ = "result_publishing"

    result_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    lab_order_id = Column(
        ForeignKey("lab_orders.id"),
        nullable=False,
    )

    result = Column(
        Text,
        nullable=False,
    )

    reference_range = Column(
        String(255),
    )

    interpretation = Column(
        Text,
    )

    approved_by = Column(
        String(150),
        nullable=False,
    )

    published_at = Column(
        DateTime,
        nullable=False,
    )

    status = Column(
        String(30),
        default="COMPLETED",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    lab_order = relationship(
        "LabOrder",
        back_populates="result_publishing",
    )