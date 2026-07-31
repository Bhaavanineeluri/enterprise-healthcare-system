from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Branch(BaseModel):

    __tablename__ = "branches"

    branch_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    hospital_id = Column(
        ForeignKey("hospitals.id"),
        nullable=False
    )

    branch_name = Column(
        String(150),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone = Column(
        String(20),
        nullable=False
    )

    address = Column(
        String(255),
        nullable=False
    )

    city = Column(
        String(100),
        nullable=False
    )

    state = Column(
        String(100),
        nullable=False
    )

    country = Column(
        String(100),
        nullable=False
    )

    postal_code = Column(
        String(20),
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    hospital = relationship(
        "Hospital",
        back_populates="branches"
    )
    departments = relationship(
        "Department",
        back_populates="branch",
        cascade="all, delete-orphan"
    )
    wards = relationship(
        "Ward",
        back_populates="branch",
        cascade="all, delete-orphan"
    )