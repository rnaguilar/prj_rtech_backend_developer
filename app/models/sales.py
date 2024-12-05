from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from datetime import datetime
from app.database import Base

class Sales(Base):
    """
    Representa a tabela Sales no banco de dados.
    """
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    qty = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="DONE")  # Status: "FAILED", "DONE"
    createdAt = Column(DateTime, default=datetime.now)
