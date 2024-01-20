from fastapi import FastAPI

from microservice.order.models.order_item import OrderItem
from microservice.order.order_service import OrderService

app = FastAPI(debug=True)


@app.post("/order/create")
def create(body: dict):
    items = [OrderItem(**item) for item in body.get("products")]
    return OrderService().create(items)


@app.get("/order/{order_id}")
def get(order_id: str):
    return OrderService().get(order_id)


@app.post("/order/update/{order_id}/{status}")
def update(order_id: str, status: str):
    return OrderService().update(order_id, status)


@app.delete("/order/{order_id}")
def delete(order_id: str):
    return OrderService().delete(order_id)
