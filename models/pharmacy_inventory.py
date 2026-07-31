from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class PharmacyInventory(BaseModel):

    __tablename__ = "pharmacy_inventory"

    pharmacy_inventory_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    medicine_name = Column(
        String(255),
        nullable=False,
    )

    generic_name = Column(
        String(255),
    )

    manufacturer = Column(
        String(255),
    )

    dosage_form = Column(
        String(100),
        nullable=False,
    )

    strength = Column(
        String(100),
        nullable=False,
    )

    batch_number = Column(
        String(100),
        unique=True,
        nullable=False,
    )

    expiry_date = Column(
        Date,
        nullable=False,
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=0,
    )

    minimum_stock = Column(
        Integer,
        nullable=False,
        default=10,
    )

    unit_price = Column(
        Numeric(10, 2),
        nullable=False,
    )

    storage_location = Column(
        String(100),
    )

    status = Column(
        String(30),
        default="AVAILABLE",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    prescription_validations = relationship(
        "PrescriptionValidation",
        back_populates="inventory",
    )

    medicine_dispensings = relationship(
        "MedicineDispensing",
        back_populates="inventory",
    )

    drug_stock_managements = relationship(
        "DrugStockManagement",
        back_populates="inventory",
    )

    batch_trackings = relationship(
        "BatchTracking",
        back_populates="inventory",
    )

    expiry_managements = relationship(
        "ExpiryManagement",
        back_populates="inventory",
    )