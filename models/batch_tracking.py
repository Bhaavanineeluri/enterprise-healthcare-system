from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class BatchTracking(BaseModel):

    __tablename__ = "batch_tracking"

    batch_tracking_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    pharmacy_inventory_id = Column(
        ForeignKey("pharmacy_inventory.id"),
        nullable=False,
    )

    manufacturing_date = Column(
        Date,
        nullable=False,
    )

    recall_status = Column(
        String(30),
        default="NOT_RECALLED",
    )

    manufacturer = Column(
        String(255),
        nullable=False,
    )

    remarks = Column(
        Text,
    )

    status = Column(
        String(30),
        default="ACTIVE",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    inventory = relationship(
        "PharmacyInventory",
        back_populates="batch_trackings",
    )