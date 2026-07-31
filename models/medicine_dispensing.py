from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class MedicineDispensing(BaseModel):

    __tablename__ = "medicine_dispensings"

    dispensing_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    prescription_validation_id = Column(
        ForeignKey("prescription_validations.id"),
        nullable=False,
    )

    pharmacy_inventory_id = Column(
        ForeignKey("pharmacy_inventory.id"),
        nullable=False,
    )

    dispensed_quantity = Column(
        Integer,
        nullable=False,
    )

    dispensed_by = Column(
        String(150),
        nullable=False,
    )

    dispensed_at = Column(
        DateTime,
        nullable=False,
    )

    remarks = Column(
        Text,
    )

    status = Column(
        String(30),
        default="DISPENSED",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    prescription_validation = relationship(
        "PrescriptionValidation",
        back_populates="medicine_dispensings",
    )

    inventory = relationship(
        "PharmacyInventory",
        back_populates="medicine_dispensings",
    )