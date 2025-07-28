from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.schemas import OrderCreate, OrderResponse
from app.validation import validate_order_business_rules

router = APIRouter()

@router.post("/create", response_model=OrderResponse)
async def create_order(order: OrderCreate = Depends(validate_order_business_rules)):
    # Simulate saving the order (e.g., to a database)
    # Here we just echo the input back
    return OrderResponse(message="Order created successfully!", order=order)
