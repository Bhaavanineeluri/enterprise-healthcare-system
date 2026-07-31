from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Document(BaseModel):

    __tablename__ = "documents"

    patient_id = Column(
        ForeignKey("patients.id"),
        nullable=False,
    )

    document_name = Column(
        String(255),
        nullable=False,
    )

    document_type = Column(
        String(100),
        nullable=False,
    )

    file_path = Column(
        String(500),
        nullable=False,
    )

    uploaded_by = Column(
        ForeignKey("users.id"),
        nullable=False,
    )
    document_code = Column(
        String(20),
        unique=True,
        nullable=False,
        index=True,
    )
    uploaded_at = Column(
        DateTime,
        nullable=False,
    )

    remarks = Column(
        Text,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    patient = relationship(
        "Patient",
        back_populates="documents",
    )

    uploader = relationship(
        "User",
    )