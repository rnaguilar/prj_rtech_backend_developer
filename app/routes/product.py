from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.product import ProductService

router = APIRouter()

@router.get("/")
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ProductService.get_products(db, skip, limit)

@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    product = ProductService.get_product_by_id(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/")
def create_product(name: str, category_id: int, price: float, db: Session = Depends(get_db)):
    return ProductService.create_product(db, name, category_id, price)

@router.delete("/{id}")
def deactivate_product(id: int, db: Session = Depends(get_db)):
    product = ProductService.deactivate_product(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deactivated successfully"}
