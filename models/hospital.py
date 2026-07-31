from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Hospital(BaseModel):

    __tablename__ = "hospitals"

    hospital_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    hospital_name = Column(
        String(150),
        nullable=False
    )

    registration_number = Column(
        String(100),
        unique=True,
        nullable=False
    )

    license_number = Column(
        String(100),
        unique=True,
        nullable=False
    )

    hospital_type = Column(
        String(100),
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

    website = Column(
        String(255)
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

    timezone = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(500)
    )

    is_active = Column(
        Boolean,
        default=True
    )

    branches = relationship(
        "Branch",
        back_populates="hospital"
    )

    branches = relationship(
        "Branch",
        back_populates="hospital",
        cascade="all, delete-orphan"
    )