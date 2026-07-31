from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class SampleCollection(BaseModel):

    __tablename__ = "sample_collections"

    sample_collection_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    lab_order_id = Column(
        ForeignKey("lab_orders.id"),
        nullable=False,
    )

    sample_type = Column(
        String(100),
        nullable=False,
    )

    sample_container = Column(
        String(100),
    )

    collected_by = Column(
        String(150),
        nullable=False,
    )

    collection_datetime = Column(
        DateTime,
        nullable=False,
    )

    remarks = Column(
        Text,
    )

    status = Column(
        String(30),
        default="COLLECTED",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    lab_order = relationship(
        "LabOrder",
        back_populates="sample_collections",
    )