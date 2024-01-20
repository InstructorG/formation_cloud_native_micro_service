from typing import List

from microservice.order.models.order import Order
from microservice.order.models.order_item import OrderItem
from microservice.order.service.services import StockService
from microservice.order.storage.command import COMMANDS


class OrderService:

    def create(self, items: List[OrderItem]):
        # 1 - Crée un object commande
        order = Order()

        # 2 - Verifie si le produit est disponible dans la marketplace
        available_items, not_available_items = StockService().check_if_all_items_are_available([item.dict() for item in items])


        # 3 - Ajout des produits disponibles à la commande
        if not_available_items.__len__() > 0:
            print(f"The following products are not available : {not_available_items}")

        # 3 - Ajout des produits disponibles à la commande
        for key, item in available_items.items():
            order.add_order_item(OrderItem(**item))

        # 4 - Enregistrer la commande
        COMMANDS[order.id] = order

        return {"message": "La commande est créé", "order": order.dict(), "not_available_items": not_available_items}

    def get(self, order_id):
        order: Order = COMMANDS.get(order_id)
        if not order:
            return {"Error": f"La commande avec l'identifant {order_id} n'existe pas ! "}
        return {"message": "La commande avec le detail", "order": order}

    def update(self, order_id, status):
        order: Order = COMMANDS.get(order_id)
        if not order:
            return {"Error": f"La commande avec l'identifant {order_id} n'existe pas ! "}
        order.change_status(status)
        COMMANDS[order_id] = order
        return {"message": "La commande est mis à jour", "order": order}

    def delete(self, order_id):
        order: Order = COMMANDS.get(order_id)
        if not order:
            return {"Error": f"La commande avec l'identifant {order_id} n'existe pas ! "}
        del COMMANDS[order_id]
        return {"message": "La commande est supprimée", "order": order_id}
