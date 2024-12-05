from sqlalchemy import Column, Integer, ForeignKey, String
from app.database import Base

class Reviwers(Base):
    """
    Representa a tabela Reviwers no banco de dados.
    """
    __tablename__ = "reviwers"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    sales_id = Column(Integer, ForeignKey("sales.id"), nullable=False)
    math = Column(Integer, nullable=False)  # Nota de 1 a 5
    description = Column(String, nullable=True)
