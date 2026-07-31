from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class TestProcessing(BaseModel):

    __tablename__ = "test_processing"

    processing_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    lab_order_id = Column(
        ForeignKey("lab_orders.id"),
        nullable=False,
    )

    processed_by = Column(
        String(150),
        nullable=False,
    )

    processing_start = Column(
        DateTime,
        nullable=False,
    )

    processing_end = Column(
        DateTime,
    )

    observations = Column(
        Text,
    )

    remarks = Column(
        Text,
    )

    status = Column(
        String(30),
        default="PROCESSING",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    lab_order = relationship(
        "LabOrder",
        back_populates="test_processing",
    )