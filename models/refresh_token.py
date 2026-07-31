from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship



from models.base_model import BaseModel

class RefreshToken(BaseModel):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True)

    token = Column(String(500), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    expires_at = Column(DateTime)

    user = relationship("User", back_populates="refresh_tokens")