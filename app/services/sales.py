# services/sales_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Sales, Stock, Product

class SalesService:
    """Service for managing sales operations."""
    
    def __init__(self, db: Session):
        """
        Initialize the SalesService with a database session.
        :param db: Database session object.
        """
        self.db = db

    def create_sale(self, client_id: int, product_id: int, qty: int) -> Sales:
        """
        Create a new sale and handle stock validation.
        :param client_id: ID of the client making the purchase.
        :param product_id: ID of the product being purchased.
        :param qty: Quantity of the product being purchased.
        :return: Created Sales object.
        """
        # Check if the product exists in stock
        stock_item = self.db.query(Stock).filter(Stock.product_id == product_id).first()
        if not stock_item:
            raise HTTPException(status_code=404, detail="Product not found in stock.")
        
        # Check if there is enough stock
        if stock_item.qty_in_stock < qty:
            # Register sale as FAILED
            sale = Sales(
                client_id=client_id,
                product_id=product_id,
                qty=qty,
                status="FAILED"
            )
            self.db.add(sale)
            self.db.commit()
            self.db.refresh(sale)
            return sale
        
        # Proceed with the sale and update stock
        stock_item.qty_in_stock -= qty
        sale = Sales(
            client_id=client_id,
            product_id=product_id,
            qty=qty,
            status="DONE"
        )
        self.db.add(sale)
        self.db.commit()
        self.db.refresh(sale)
        self.db.commit()
        return sale

    def get_sales(self, sale_id: int = None):
        """
        Retrieve sales data. If sale_id is None, fetch all sales.
        :param sale_id: Optional ID of a specific sale to fetch.
        :return: Sale or list of sales.
        """
        if sale_id:
            sale = self.db.query(Sales).filter(Sales.id == sale_id).first()
            if not sale:
                raise HTTPException(status_code=404, detail="Sale not found.")
            return sale
        
        # Return all sales
        return self.db.query(Sales).all()

    def delete_sale(self, sale_id: int):
        """
        Mark a sale as inactive.
        :param sale_id: ID of the sale to delete.
        """
        sale = self.db.query(Sales).filter(Sales.id == sale_id).first()
        if not sale:
            raise HTTPException(status_code=404, detail="Sale not found.")
        sale.status = "FAILED"
        self.db.commit()
