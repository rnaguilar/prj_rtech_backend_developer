from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.reviewers import ReviwersService

router = APIRouter()

@router.get("/")
def get_reviwers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ReviwersService.get_reviwers(db, skip, limit)

@router.get("/{id}")
def get_reviwer_by_id(id: int, db: Session = Depends(get_db)):
    reviwer = ReviwersService.get_reviwer_by_id(db, id)
    if not reviwer:
        raise HTTPException(status_code=404, detail="Reviwer not found")
    return reviwer

@router.post("/")
def create_reviwer(client_id: int, sales_id: int, math: int, description: str, db: Session = Depends(get_db)):
    return ReviwersService.create_reviwer(db, client_id, sales_id, math, description)

@router.delete("/{id}")
def delete_reviwer(id: int, db: Session = Depends(get_db)):
    reviwer = ReviwersService.delete_reviwer(db, id)
    if not reviwer:
        raise HTTPException(status_code=404, detail="Reviwer not found")
    return {"message": "Reviwer deleted successfully"}
