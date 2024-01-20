from database.models.models import OrderModel, OrderItemModel
from core.domain.order import Order

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

products_db = []

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def create_product(product: Product):
    products_db.append(product)
    return {"message": "Product added successfully"}


class OrderRepository:
    def __init__(self, session):
        self.session = session

    def add(self, items):
        record = OrderModel(items=[OrderItemModel(**item) for item in items])
        self.session.add(record)
        return Order(**record.dict(), order_=record)

    def _get(self, model, id_):
        return self.session.query(model).filter(model.id == str(id_)).first()

    def get(self, id_):
        order = self._get(OrderModel, id_)
        if order is not None:
            return Order(**order.dict())

    def update(self, id_, payload):
        record = self._get(OrderModel, id_)
        if 'items' in payload:
            for item in record.items:
                self.session.delete(item)
            breakpoint()
            record.items = [OrderItemModel(**item) for item in payload.pop('items')]
        for key, value in payload.items():
            setattr(record, key, value)
        self.session.add(record)
        return Order(**record.dict())

    def list(self, limit=None, **filters):
        query = self.session.query(OrderModel)
        records = query.filter_by(**filters).limit(limit).all()
        return [Order(**record.dict()) for record in records]

    def delete(self, id_, is_item=False):
        model = OrderItemModel if is_item else OrderModel
        self.session.delete(self._get(model, id_))
