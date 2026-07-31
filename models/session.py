from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.connection import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    login_time = Column(DateTime, default=datetime.utcnow)

    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="sessions")