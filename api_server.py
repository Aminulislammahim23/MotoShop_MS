# ============================================
# api_server.py - MotoShop Server API
# ============================================

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(
    title="MotoShop API Server",
    description="Simple dictionary-based MotoShop API",
    version="1.0.0"
)

# Fake DB (In-memory dictionary list)
products_db = []


# -------- MODEL CLASS --------
class ProductModel(BaseModel):
    id: int
    name: str
    price: float
    qty: int


# -------- 1) ADD PRODUCT (POST) --------
@app.post("/add_product")
def add_product(product: ProductModel):
    products_db.append(product.dict())
    return {
        "message": "Product added successfully",
        "product": product
    }


# -------- 2) LIST ALL PRODUCTS (GET) --------
@app.get("/list_products")
def list_products():
    return {
        "total": len(products_db),
        "products": products_db
    }


# -------- 3) SEARCH PRODUCT BY NAME --------
@app.get("/search_product")
def search_product(name: str = Query(...)):
    result = [p for p in products_db if p["name"].lower() == name.lower()]

    return {
        "search_name": name,
        "found": len(result),
        "results": result
    }


# -------- 4) TOTAL INVENTORY VALUE --------
@app.get("/total_value")
def total_value():
    total = sum([p["price"] * p["qty"] for p in products_db])

    return {
        "total_inventory_value": total,
        "product_count": len(products_db)
    }


# Run: uvicorn api_server:app --reload --port 8000
