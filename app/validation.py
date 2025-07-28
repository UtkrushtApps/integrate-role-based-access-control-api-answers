from fastapi import Depends, HTTPException, status
from app.schemas import OrderCreate, OrderItem
from typing import List

# Example business rules
RESTRICTED_ITEMS = {"restricted_item", "prohibited_goods"}
MAX_QUANTITY_PER_ITEM = 20


def validate_order_business_rules(order: OrderCreate = Depends()) -> OrderCreate:
    errors = {}
    for idx, item in enumerate(order.items):
        item_errors = []
        # Rule 1: Restricted item check
        if item.name in RESTRICTED_ITEMS:
            item_errors.append(f"Item '{item.name}' is restricted and cannot be ordered.")
        # Rule 2: Quantity limit check
        if item.quantity > MAX_QUANTITY_PER_ITEM:
            item_errors.append(f"Quantity for item '{item.name}' exceeds the limit ({MAX_QUANTITY_PER_ITEM}).")
        if item.quantity <= 0:
            item_errors.append(f"Quantity for item '{item.name}' must be greater than 0.")
        if item_errors:
            errors[f"items[{idx}]"] = item_errors

    # Global order checks (add more as needed)
    if not order.items:
        errors["items"] = ["Order must contain at least one item."]

    if errors:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={"errors": errors}
        )
    return order
