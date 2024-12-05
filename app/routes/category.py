from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.category import CategoryService
from database import get_db

router = APIRouter()

@router.get("/")
def get_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retorna categorias paginadas.
    """
    return CategoryService.get_categories(db, skip, limit)

@router.get("/{id}")
def get_category(id: int, db: Session = Depends(get_db)):
    """
    Retorna uma categoria pelo ID.
    """
    category = CategoryService.get_category_by_id(db, id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.post("/")
def create_category(name: str, db: Session = Depends(get_db)):
    """
    Cria uma nova categoria.
    """
    return CategoryService.create_category(db, name)

@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    """
    Marca uma categoria como inativa.
    """
    category = CategoryService.deactivate_category(db, id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": f"Category with ID {id} marked as inactive"}
