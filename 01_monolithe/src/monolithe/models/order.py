from enum import Enum
from typing import List
from uuid import uuid4

from src.monolithe.models.order_item import OrderItem
from src.monolithe.storage.stocks import STOCK_STORAGE


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


AVAILABLE_STOCKS = ["Paris", "Marseille", "Lyon", "Lille"]


class Order:
    id: str
    status: StatusEnum
    order_items: any = []
    stock_items = STOCK_STORAGE

    def __init__(self, id=uuid4().__str__(), status=StatusEnum.created):
        self.id = id
        self.status = status
        self._init_stock()

    def check_if_all_items_are_available(self, items: List[OrderItem], available_items: dict):
        not_available_items = [item.name for item in items if not available_items.get(f"{item.name}_{item.type}")]

        if not_available_items.__len__() > 0:
            # Remplacer le code à ce niveau
            print(f"Les produits suivants ne sont pas disponibles : {not_available_items}")

    def _init_stock(self):
        stock_cities = [content.get("city") for magasin, content in self.stock_items.items()]
        if sorted(stock_cities) != sorted(AVAILABLE_STOCKS):
            raise Exception("SOME STOCKS ARE NOT AVAILABLE")
        return STOCK_STORAGE

    def add_order_item(self, item: OrderItem):
        if item.stock.get("city") not in AVAILABLE_STOCKS:
            raise Exception("STOCK IS NOT PRESENT IN LIST", item.stock)
        self.order_items.append(item)

    def change_status(self, status):
        self.status = status

    def dict(self):
        return {
            'id': self.id,
            'status': self.status.name,
            'order_items': [item.dict() for item in self.order_items],
        }
