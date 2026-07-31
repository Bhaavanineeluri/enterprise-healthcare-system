from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


class OTP(BaseModel):
    __tablename__ = "otps"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    otp_code = Column(
        String(6),
        nullable=False,
    )

    purpose = Column(
        String(30),
        nullable=False,
    )

    is_verified = Column(
        Boolean,
        default=False,
    )

    expires_at = Column(
        DateTime,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship(
        "User",
        back_populates="otps",
    )