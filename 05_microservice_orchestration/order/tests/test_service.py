import pytest

from order.src.microservice.order.models.order_item import OrderItem
from order.src.microservice.order.order_service import OrderService


def test_create_command():
    # Given
    order_items = [
        OrderItem(name="levis", type="pantalon", quantity=3),
        OrderItem(name="decathlon", type="chaussette", quantity=3),
        OrderItem(name="nike", type="casquette", quantity=3)
    ]

    # When
    response = OrderService().create(order_items)

    # Then
    order = response.get("order")
    assert order.get("status") == 'created'
    assert order.get("order_items") == [{'name': 'levis', 'type': 'pantalon', 'quantity': 3},
                                        {'name': 'decathlon', 'type': 'chaussette', 'quantity': 3},
                                        {'name': 'nike', 'type': 'casquette', 'quantity': 3}]


def test_create_command_when_items_are_not_present():
    # Given
    order_items = [
        OrderItem(name="jule", type="jean", quantity=10)
    ]

    # When
    with pytest.raises(Exception) as e:
        OrderService().create(order_items)

    # Then

    assert e.value.__str__() == '{\'status\': \'failed\', \'message\': "Les produits suivants ne sont pas disponibles : [\'jule\']"}'
