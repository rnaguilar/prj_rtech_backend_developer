from sqlalchemy.orm import Session
from models.reviewers import Reviwers

class ReviwersService:
    """
    Serviço para operações relacionadas à tabela Reviwers.
    """

    @staticmethod
    def get_reviwers(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Reviwers).offset(skip).limit(limit).all()

    @staticmethod
    def get_reviwer_by_id(db: Session, id: int):
        return db.query(Reviwers).filter(Reviwers.id == id).first()

    @staticmethod
    def create_reviwer(db: Session, client_id: int, sales_id: int, math: int, description: str = None):
        new_reviwer = Reviwers(client_id=client_id, sales_id=sales_id, math=math, description=description)
        db.add(new_reviwer)
        db.commit()
        db.refresh(new_reviwer)
        return new_reviwer

    @staticmethod
    def delete_reviwer(db: Session, id: int):
        reviwer = db.query(Reviwers).filter(Reviwers.id == id).first()
        if reviwer:
            db.delete(reviwer)
            db.commit()
        return reviwer
