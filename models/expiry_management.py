from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ExpiryManagement(BaseModel):

    __tablename__ = "expiry_management"

    expiry_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    pharmacy_inventory_id = Column(
        ForeignKey("pharmacy_inventory.id"),
        nullable=False,
    )

    review_date = Column(
        Date,
        nullable=False,
    )

    expiry_status = Column(
        String(30),
        nullable=False,
    )

    reviewed_by = Column(
        String(150),
        nullable=False,
    )

    remarks = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    inventory = relationship(
        "PharmacyInventory",
        back_populates="expiry_managements",
    )