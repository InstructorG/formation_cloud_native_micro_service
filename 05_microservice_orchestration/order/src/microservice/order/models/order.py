from enum import Enum
from uuid import uuid4

from microservice.order.models.order_item import OrderItem


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class Order:
    id: str
    status: StatusEnum
    order_items: any = []

    def __init__(self, id=uuid4().__str__(), status=StatusEnum.created):
        self.id = id
        self.status = status

    def add_order_item(self, item: OrderItem):
        self.order_items.append(item)

    def change_status(self, status):
        self.status = status

    def dict(self):
        return {
            'id' : self.id,
            'status': self.status.name,
            'order_items': [item.dict() for item in self.order_items],
        }
