from sqlalchemy.orm import Session
from models.stock import Stock
from datetime import datetime

class StockService:
    """
    Serviço para operações relacionadas à tabela Stock.
    """

    @staticmethod
    def get_stocks(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Stock).filter(Stock.active == True).offset(skip).limit(limit).all()

    @staticmethod
    def get_stock_by_product_id(db: Session, product_id: int):
        return db.query(Stock).filter(Stock.product_id == product_id, Stock.active == True).first()

    @staticmethod
    def create_stock(db: Session, product_id: int, qty_in_stock: int):
        new_stock = Stock(product_id=product_id, qty_in_stock=qty_in_stock, createdAt=datetime.now())
        db.add(new_stock)
        db.commit()
        db.refresh(new_stock)
        return new_stock

    @staticmethod
    def deactivate_stock(db: Session, product_id: int):
        stock = db.query(Stock).filter(Stock.product_id == product_id).first()
        if stock:
            stock.active = False
            stock.updatedAt = datetime.now()
            db.commit()
        return stock
