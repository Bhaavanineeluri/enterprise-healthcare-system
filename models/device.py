from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Device(BaseModel):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    device_name = Column(String(200))

    ip_address = Column(String(100))

    browser = Column(String(100))

    operating_system = Column(String(100))

    user = relationship("User", back_populates="devices")