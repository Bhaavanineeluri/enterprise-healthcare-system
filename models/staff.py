from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Staff(BaseModel):

    __tablename__ = "staff"

    staff_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True
    )

    department_id = Column(
        ForeignKey("departments.id"),
        nullable=False
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    gender = Column(
        String(20),
        nullable=False
    )

    designation = Column(
        String(100),
        nullable=False
    )

    employee_type = Column(
        String(50),
        nullable=False
    )

    qualification = Column(
        String(150)
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

    joining_date = Column(
        String(20),
        nullable=False
    )

    status = Column(
        String(30),
        default="Active"
    )

    is_active = Column(
        Boolean,
        default=True
    )

    department = relationship(
        "Department",
        back_populates="staff_members"
    )