from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.client import ClientService

router = APIRouter()

@router.get("/")
def get_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ClientService.get_clients(db, skip, limit)

@router.get("/{id}")
def get_client(id: int, db: Session = Depends(get_db)):
    client = ClientService.get_client_by_id(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.post("/")
def create_client(name: str, email: str, db: Session = Depends(get_db)):
    return ClientService.create_client(db, name, email)

@router.delete("/{id}")
def delete_client(id: int, db: Session = Depends(get_db)):
    client = ClientService.delete_client(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}
