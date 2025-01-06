from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Decimal
from db import Base

class products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    stock = Column(Integer, index=True)
    price = Column(Decimal, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)