from sqlalchemy import Column, Integer, String
from app.database import Base

class Client(Base):
    """
    Representa a tabela Client no banco de dados.
    """
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
