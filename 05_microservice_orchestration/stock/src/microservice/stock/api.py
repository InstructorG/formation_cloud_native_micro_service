from fastapi import FastAPI

from microservice.stock.models.order_item import OrderItem
from microservice.stock.stock_service import StockService

app = FastAPI(debug=True)


@app.post("/stock/check")
def check(body: dict):
    items = [OrderItem(**item) for item in body.get("items")]
    return StockService().check(items)

@app.post("/stock/add")
def add(body: dict):
    magasin = body.get("magasin")
    return StockService().add(magasin)

@app.post("/stock/add")
def delete(body: dict):
    magasin = body.get("magasin")
    return StockService().delete(magasin)


@app.post("/stock/update")
def update(body: dict):
    magasin = body.get("magasin")
    return StockService().update(magasin)