"""
Product Catalog API using FastAPI
Starter code for the REST APIs with FastAPI assignment
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# Define a Product model for request/response validation
class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    description: str

# Sample data - you'll replace this with file-based persistence
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "description": "High-performance laptop"},
    {"id": 2, "name": "Mouse", "price": 29.99, "description": "Wireless mouse"},
    {"id": 3, "name": "Keyboard", "price": 79.99, "description": "Mechanical keyboard"},
]

# TODO: Task 1 - Complete the root endpoint
@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Welcome to the Product Catalog API"}

# TODO: Task 1 - Complete the GET /products endpoint
@app.get("/products")
def list_products():
    """Return all products"""
    return products

# TODO: Task 2 - Implement POST /products endpoint to add a new product
@app.post("/products")
def create_product(product: Product):
    """Add a new product to the catalog"""
    # Your implementation here
    pass

# TODO: Task 2 - Implement GET /products/{product_id} endpoint
@app.get("/products/{product_id}")
def get_product(product_id: int):
    """Retrieve a specific product by ID"""
    # Your implementation here
    pass

# TODO: Task 2 - Implement PUT /products/{product_id} endpoint
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    """Update an existing product"""
    # Your implementation here
    pass

# TODO: Task 2 - Implement DELETE /products/{product_id} endpoint
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Delete a product from the catalog"""
    # Your implementation here
    pass

# TODO: Task 3 - Add filtering with query parameters
# Hint: Modify list_products() to accept optional min_price and max_price parameters

# TODO: Task 3 - Add file persistence
# Hint: Save products to products.json after modifications
# Hint: Load products from products.json on server startup

# To run this server:
# 1. Install dependencies: pip install fastapi uvicorn
# 2. Start the server: uvicorn starter_code:app --reload
# 3. Visit http://localhost:8000 or http://localhost:8000/docs for interactive API documentation
