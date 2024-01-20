from fastapi import FastAPI

from src.monolithe.models.order_item import OrderItem
from src.monolithe.service import Service

app = FastAPI(debug=True)


@app.post("/command")
def order(body: dict):
    items = [OrderItem(**item) for item in body.get("products")]
    return Service().create_command(items)


@app.post("/pay/{order_id}")
def pay(order_id: str):
    return Service().pay_command(order_id)


@app.post("/schedule/{order_id}")
def schedule(order_id: str):
    return Service().schedule_command(order_id)
