from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.sales import SalesService

router = APIRouter()


@router.get("/")
def get_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return SalesService.get_sales(db, skip, limit)

@router.get("/{id}")
def get_sales_by_id(id: int, db: Session = Depends(get_db)):
    sales = SalesService.get_sales_by_id(db, id)
    if not sales:
        raise HTTPException(status_code=404, detail="Sales not found")
    return sales

@router.post("/")
def create_sales(client_id: int, product_id: int, qty: int, db: Session = Depends(get_db)):
    return SalesService.create_sales(db, client_id, product_id, qty)

@router.delete("/{id}")
def delete_sales(id: int, db: Session = Depends(get_db)):
    sales = SalesService.delete_sales(db, id)
    if not sales:
        raise HTTPException(status_code=404, detail="Sales not found")
    return {"message": "Sales deleted successfully"}
