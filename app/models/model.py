from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from db import Base

class model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)