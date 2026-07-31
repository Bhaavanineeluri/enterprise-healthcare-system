from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class PrescriptionValidation(BaseModel):

    __tablename__ = "prescription_validations"

    validation_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )

    prescription_id = Column(
        ForeignKey("prescriptions.id"),
        nullable=False,
    )

    pharmacy_inventory_id = Column(
        ForeignKey("pharmacy_inventory.id"),
        nullable=False,
    )

    requested_quantity = Column(
        Integer,
        nullable=False,
    )

    approved_quantity = Column(
        Integer,
        nullable=False,
    )

    validation_status = Column(
        String(30),
        default="VALIDATED",
    )

    remarks = Column(
        Text,
    )

    validated_by = Column(
        String(150),
        nullable=False,
    )

    validation_date = Column(
        DateTime,
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    prescription = relationship(
        "Prescription",
        back_populates="prescription_validations",
    )

    inventory = relationship(
        "PharmacyInventory",
        back_populates="prescription_validations",
    )
    medicine_dispensings = relationship(
        "MedicineDispensing",
        back_populates="prescription_validation",
    )