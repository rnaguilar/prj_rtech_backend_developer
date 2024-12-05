from sqlalchemy.orm import Session
from models.client import Client

class ClientService:
    """
    Serviço para operações relacionadas à tabela Client.
    """

    @staticmethod
    def get_clients(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Client).offset(skip).limit(limit).all()

    @staticmethod
    def get_client_by_id(db: Session, id: int):
        return db.query(Client).filter(Client.id == id).first()

    @staticmethod
    def create_client(db: Session, name: str, email: str):
        new_client = Client(name=name, email=email)
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client

    @staticmethod
    def delete_client(db: Session, id: int):
        client = db.query(Client).filter(Client.id == id).first()
        if client:
            db.delete(client)
            db.commit()
        return client
