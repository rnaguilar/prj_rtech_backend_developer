from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.stock import StockService

router = APIRouter()


@router.get("/")
def get_stocks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return StockService.get_stocks(db, skip, limit)

@router.get("/{product_id}")
def get_stock(product_id: int, db: Session = Depends(get_db)):
    stock = StockService.get_stock_by_product_id(db, product_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return stock

@router.post("/")
def create_stock(product_id: int, qty_in_stock: int, db: Session = Depends(get_db)):
    return StockService.create_stock(db, product_id, qty_in_stock)

@router.delete("/{product_id}")
def deactivate_stock(product_id: int, db: Session = Depends(get_db)):
    stock = StockService.deactivate_stock(db, product_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    return {"message": "Stock deactivated successfully"}
