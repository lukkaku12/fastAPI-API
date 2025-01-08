from decimal import Decimal  # Asegúrate de importar decimal
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Numeric, Index  # Cambiar Decimal por Numeric
from models.db import Base

class Product(Base):
    __tablename__ = "products"
    __table_args__ = (
        Index('ix_products_name', 'name', unique=True),  # Si quieres un índice único
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    stock = Column(Integer, index=True)
    price = Column(Numeric, index=True)  # Cambia Decimal por Numeric
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

     
    __table_args__ = {'extend_existing': True}