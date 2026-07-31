from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Department(BaseModel):

    __tablename__ = "departments"

    department_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    branch_id = Column(
        ForeignKey("branches.id"),
        nullable=False
    )

    department_name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(255)
    )

    phone = Column(
        String(20)
    )

    email = Column(
        String(100),
        unique=True
    )

    location = Column(
        String(100)
    )

    is_active = Column(
        Boolean,
        default=True
    )

    branch = relationship(
        "Branch",
        back_populates="departments"
    )

    doctors = relationship(
        "Doctor",
        back_populates="department",
        cascade="all, delete-orphan"
    )
    staff_members = relationship(
        "Staff",
        back_populates="department",
        cascade="all, delete-orphan"
    )
    appointments = relationship(
        "Appointment",
        back_populates="department",
    )
    opd_records = relationship(
        "OPD",
        back_populates="department",
    )
    ipd_records = relationship(
        "IPD",
        back_populates="department",
    )