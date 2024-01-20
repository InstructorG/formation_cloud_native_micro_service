from typing import List

from src.monolithe.models.order import Order, StatusEnum
from src.monolithe.models.stock_item import StockItem
from src.monolithe.models.order_item import OrderItem
from src.monolithe.storage.command import COMMANDS


class Service:

    def create_command(self, items: List[OrderItem]):
        # 1 - Crée un object commande
        order = Order()

        # 2 - Verifie si le produit est disponible dans la marketplace
        available_items = {}
        for item in items:

            for magasin, content in order.stock_items.items():
                stock_item = self.check_if_item_is_available(content, item)

                if not stock_item:
                    continue

                if stock_item.quantity < item.quantity:
                    continue

                item.add_stock_item(content)
                available_items[f"{item.name}_{item.type}"] = item
                break

        # 3 - Verifie si le produit est disponible dans la marketplace
        order.check_if_all_items_are_available(items, available_items)

        for key, item in available_items.items():
            order.add_order_item(item)

        # 3 - Stockage de la commande
        COMMANDS[order.id] = order

        return {"message": "La commande est créé", "order": order.dict()}

    def check_if_item_is_available(self, stock, item) -> StockItem:
        for stock_item in stock.get("items"):
            if item.name == stock_item.get("name"):
                return StockItem(**stock_item)

    def pay_command(self, order_id):
        order = COMMANDS.get(order_id)
        if not order:
            return {"Error": f"La commande avec l'identifant {order_id} n'existe pas ! "}
        order.change_status(StatusEnum.paid)
        COMMANDS[order.id] = order
        return {"message": "La commande est payé", "order": order}

    def schedule_command(self, order_id):
        order: Order = COMMANDS.get(order_id)
        if not order:
            return {"Error": f"La commande avec l'identifant {order_id} n'existe pas ! "}
        if order.status.name != "paid":
            return {"Error": f"La commande avec l'identifant {order_id} n'est pas encore payé ! "}
        order.change_status(StatusEnum.dispatched)
        COMMANDS[order.id] = order
        return {"message": "La commande est programmé pour une livraison", "order": order}
