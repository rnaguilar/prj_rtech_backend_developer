from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime
from datetime import datetime
from app.database import Base

class Stock(Base):
    """
    Representa a tabela Stock no banco de dados.
    """
    __tablename__ = "stock"

    product_id = Column(Integer, ForeignKey("product.id"), primary_key=True, index=True)
    qty_in_stock = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, nullable=True)
