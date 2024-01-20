from typing import List

from stock.src.microservice.stock.models.order_item import OrderItem
from stock.src.microservice.stock.models.stock_item import StockItem
from stock.src.microservice.stock.storage.stocks import STOCK_STORAGE


class StockService:

    def check(self, items: List[OrderItem]):
        available_items = {}
        for item in items:
            for magasin, content in STOCK_STORAGE.items():
                stock_item = self.check_if_item_is_available(content, item)

                if not stock_item:
                    continue

                if stock_item.quantity < item.quantity:
                    continue

                item.add_stock_item(stock_item)

                available_items[f'{item.name}_{item.type}'] = item
                break

        not_available_items = [item.name for item in items if not available_items.get(f"{item.name}_{item.type}")]

        return {"available": available_items, "not_available_items": not_available_items}

    def check_if_item_is_available(self, stock, item) -> StockItem:
        for stock_item in stock.get("items"):
            if item.name == stock_item.get("name"):
                return StockItem(**stock_item)

    def add(self, magasin):
        STOCK_STORAGE[magasin.get("name")] = magasin
        return {"message": "magasin ajouté", "magasin": magasin}

    def delete(self, magasin):
        del STOCK_STORAGE[magasin.get("name")]
        return {"message": "magasin supprimé", "magasin": magasin}

    def update(self, magasin):
        STOCK_STORAGE[magasin.get("name")] = magasin
        return {"message": "magasin mis à jour", "magasin": magasin}
