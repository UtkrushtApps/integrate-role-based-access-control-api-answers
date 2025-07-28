from pydantic import BaseModel, Field
from typing import List, Literal

class OrderItem(BaseModel):
    name: str = Field(..., example="item001")
    quantity: int = Field(..., gt=0, le=100, example=1)

class OrderCreate(BaseModel):
    customer_id: str = Field(..., example="cust1234")
    items: List[OrderItem]

class OrderResponse(BaseModel):
    message: str
    order: OrderCreate
