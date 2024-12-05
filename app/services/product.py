from sqlalchemy.orm import Session
from models.product import Product
from datetime import datetime

class ProductService:
    """
    Serviço para operações relacionadas à tabela Product.
    """

    @staticmethod
    def get_products(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Product).filter(Product.active == True).offset(skip).limit(limit).all()

    @staticmethod
    def get_product_by_id(db: Session, id: int):
        return db.query(Product).filter(Product.id == id, Product.active == True).first()

    @staticmethod
    def create_product(db: Session, name: str, category_id: int, price: float):
        new_product = Product(name=name, category_id=category_id, price=price, createdAt=datetime.now())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product

    @staticmethod
    def deactivate_product(db: Session, id: int):
        product = db.query(Product).filter(Product.id == id).first()
        if product:
            product.active = False
            product.updatedAt = datetime.now()
            db.commit()
        return product
