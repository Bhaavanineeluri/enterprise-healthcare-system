from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class DrugStockManagement(BaseModel):

    __tablename__ = "drug_stock_management"

    stock_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    pharmacy_inventory_id = Column(
        ForeignKey("pharmacy_inventory.id"),
        nullable=False,
    )

    transaction_type = Column(
        String(30),
        nullable=False,
    )

    quantity = Column(
        Integer,
        nullable=False,
    )

    previous_quantity = Column(
        Integer,
        nullable=False,
    )

    updated_quantity = Column(
        Integer,
        nullable=False,
    )

    remarks = Column(
        Text,
    )

    updated_by = Column(
        String(150),
        nullable=False,
    )

    updated_at = Column(
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

    inventory = relationship(
        "PharmacyInventory",
        back_populates="drug_stock_managements",
    )