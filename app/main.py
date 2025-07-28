from fastapi import FastAPI
from app.routers import orders

app = FastAPI(title="Order Management Service")

app.include_router(orders.router, prefix="/orders", tags=["orders"])
