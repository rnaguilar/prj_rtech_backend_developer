from fastapi import FastAPI
from routes.category import category_router
from routes.product import product_router
from routes.stock import stock_router
from routes.client import client_router
from routes.sales import sales_router
from routes.reviewers import reviewers_router
from database import Base, engine

app = FastAPI(title="E-commerce API", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(category_router, prefix="/category", tags=["Category"])
app.include_router(product_router, prefix="/product", tags=["Product"])
app.include_router(stock_router, prefix="/stock", tags=["Stock"])
app.include_router(client_router, prefix="/client", tags=["Client"])
app.include_router(sales_router, prefix="/sales", tags=["Sales"])
app.include_router(reviewers_router, prefix="/reviewers", tags=["Reviwers"])
