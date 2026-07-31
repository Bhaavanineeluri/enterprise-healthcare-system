from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Ward(BaseModel):

    __tablename__ = "wards"

    ward_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    branch_id = Column(
        ForeignKey("branches.id"),
        nullable=False
    )

    ward_name = Column(
        String(100),
        nullable=False
    )

    ward_type = Column(
        String(50),
        nullable=False
    )

    floor = Column(
        Integer,
        nullable=False
    )

    capacity = Column(
        Integer,
        nullable=False
    )

    occupied_beds = Column(
        Integer,
        default=0
    )

    incharge_name = Column(
        String(100)
    )

    phone = Column(
        String(20)
    )

    description = Column(
        String(255)
    )

    is_active = Column(
        Boolean,
        default=True
    )

    branch = relationship(
        "Branch",
        back_populates="wards"
    )

    rooms = relationship(
        "Room",
        back_populates="ward",
        cascade="all, delete-orphan"
    )
    
    ipd_records = relationship(
        "IPD",
        back_populates="ward",
    )