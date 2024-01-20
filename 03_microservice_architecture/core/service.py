from database.respository import OrderRepository
from core.exceptions import OrderNotFoundError


class OrderService:
    def __init__(self, orders_repository: OrderRepository):
        self.orders_repository = orders_repository

    def create_order(self, items):
        return self.orders_repository.add(items)

    def get_order(self, order_id):
        order = self.orders_repository.get(order_id)
        if order is not None:
            return order
        raise OrderNotFoundError(f'Order with id {order_id} not found')

    def replace_order(self, order_id, payload):
        order = self.orders_repository.get(order_id)
        if order is None:
            raise OrderNotFoundError(f'Order with id {order_id} not found')
        return self.orders_repository.update(order_id, payload)

    def list_orders(self, **filters):
        limit = filters.pop('limit', None)
        return self.orders_repository.list(limit, **filters)

    def delete_order(self, order_id):
        order = self.orders_repository.get(order_id)
        if order is None:
            raise OrderNotFoundError(f'Order with id {order_id} not found')
        for item in order.items:
            self.orders_repository.delete(item.id, True)
        return self.orders_repository.delete(order_id)