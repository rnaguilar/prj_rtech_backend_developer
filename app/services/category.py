from sqlalchemy.orm import Session
from models.category import Category
from datetime import datetime

class CategoryService:
    """
    Lida com as operações no banco de dados relacionadas à tabela Category.
    """
    @staticmethod
    def get_categories(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Category).filter(Category.active == True).offset(skip).limit(limit).all()

    @staticmethod
    def get_category_by_id(db: Session, id: int):
        return db.query(Category).filter(Category.id == id, Category.active == True).first()

    @staticmethod
    def create_category(db: Session, name: str):
        new_category = Category(name=name, createdAt=datetime.now())
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category

    @staticmethod
    def deactivate_category(db: Session, id: int):
        category = db.query(Category).filter(Category.id == id).first()
        if category:
            category.active = False
            category.updatedAt = datetime.now()
            db.commit()
        return category
