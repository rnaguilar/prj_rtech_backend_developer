from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, DateTime
from datetime import datetime
from app.database import Base

class Product(Base):
    """
    Representa a tabela Product no banco de dados.
    """
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    price = Column(Float, nullable=False)
    active = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, nullable=True)
