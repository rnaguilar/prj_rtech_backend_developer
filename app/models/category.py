from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class Category(Base):
    """
    Representa a tabela Category no banco de dados.
    """
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.now)
    updatedAt = Column(DateTime, nullable=True)
