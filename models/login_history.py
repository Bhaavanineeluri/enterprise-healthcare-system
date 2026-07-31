from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from models.base_model import BaseModel
class LoginHistory(BaseModel):
    __tablename__ = "login_history"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    login_time = Column(DateTime, default=datetime.utcnow)

    status = Column(String(50))

    user = relationship("User", back_populates="login_history")