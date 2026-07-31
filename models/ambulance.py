from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String

from models.base_model import BaseModel


class Ambulance(BaseModel):

    __tablename__ = "ambulances"

    ambulance_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    vehicle_number = Column(
        String(30),
        unique=True,
        nullable=False
    )

    vehicle_type = Column(
        String(50),
        nullable=False
    )

    driver_name = Column(
        String(100),
        nullable=False
    )

    driver_phone = Column(
        String(20),
        nullable=False
    )

    current_location = Column(
        String(255)
    )

    status = Column(
        String(30),
        default="AVAILABLE"
    )

    is_active = Column(
        Boolean,
        default=True
    )