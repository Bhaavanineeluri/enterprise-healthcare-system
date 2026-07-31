from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Bed(BaseModel):

    __tablename__ = "beds"

    bed_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    room_id = Column(
        ForeignKey("rooms.id"),
        nullable=False
    )

    patient_id = Column(
        ForeignKey("patients.id"),
        nullable=True
    )

    bed_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    bed_type = Column(
        String(50),
        nullable=False
    )

    bed_status = Column(
        String(30),
        default="AVAILABLE"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    room = relationship(
        "Room",
        back_populates="beds"
    )

    patient = relationship(
        "Patient"
    )
    ipd_record = relationship(
        "IPD",
        back_populates="bed",
        uselist=False,
    )