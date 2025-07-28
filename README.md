1. **Set up Pydantic Schemas**
   - Create Pydantic models for `OrderItem`, `OrderCreate`, and `OrderResponse` in `app/schemas.py`.
   - Define required fields and constraints (e.g., quantity > 0).

2. **Centralize Validation Logic**
   - Implement `validate_order_business_rules` in `app/validation.py`.
   - This function serves as a FastAPI dependency and checks:
     - No order contains restricted items (e.g., 'restricted_item').
     - No item exceeds `MAX_QUANTITY_PER_ITEM` (e.g., 20).
     - Quantities are always positive.
   - Collect errors by field. If any are present, raise `HTTPException` with a structured error payload.

3. **Uniform Dependency Injection**
   - In `app/routers/orders.py`, use `Depends(validate_order_business_rules)` in all order-related endpoints.
   - The validator ensures all relevant endpoints enforce business rules identically.

4. **Order Endpoint Response Structure**
   - Return a standardized `OrderResponse` containing the input order and a success message.
   - Errors are handled by FastAPI’s exception system and return field-specific details as specified by the validator.

5. **API Routing**
   - Use FastAPI routers in `app/routers/orders.py` and include in `app/main.py` with appropriate prefixes.

6. **Dockerization**
   - Create a `Dockerfile` that installs dependencies from `requirements.txt`, sets work directories, and runs the FastAPI app via `uvicorn`.

7. **Reproducibility**
   - Add all dependencies to `requirements.txt`.

8. **Run the Application**
   - Build and run the Docker container for a reproducible, isolated deployment.