from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base_model import BaseModel
from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    username = Column(String(50), unique=True, nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role_id = Column(Integer, ForeignKey("roles.id"))

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role", back_populates="users")

    refresh_tokens = relationship("RefreshToken", back_populates="user")

    sessions = relationship("Session", back_populates="user")

    devices = relationship("Device", back_populates="user")

    login_history = relationship("LoginHistory", back_populates="user")

    audit_logs = relationship("AuditLog", back_populates="user")

    otps = relationship("OTP",back_populates="user",)