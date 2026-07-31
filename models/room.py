from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Room(BaseModel):

    __tablename__ = "rooms"

    room_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    ward_id = Column(
        ForeignKey("wards.id"),
        nullable=False
    )

    room_number = Column(
        String(20),
        unique=True,
        nullable=False
    )

    room_type = Column(
        String(50),
        nullable=False
    )

    floor = Column(
        Integer,
        nullable=False
    )

    total_beds = Column(
        Integer,
        nullable=False
    )

    occupied_beds = Column(
        Integer,
        default=0
    )

    room_status = Column(
        String(30),
        default="AVAILABLE"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    ward = relationship(
        "Ward",
        back_populates="rooms"
    )

    beds = relationship(
        "Bed",
        back_populates="room",
        cascade="all, delete-orphan"
    )
    ipd_records = relationship(
        "IPD",
        back_populates="room",
    )