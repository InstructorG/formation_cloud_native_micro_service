from typing import List, Union

from starlette import status
from fastapi import HTTPException, APIRouter
import os

from database.respository import OrderRepository
from database.storage_context_manager import StorageContextManager
from core.exceptions import OrderNotFoundError
from core.service import OrderService
from web.schema.order import OrderSchema

router = r = APIRouter()

DATABASE_CONNEXION = os.getenv("DATABASE_CONNEXION", default="sqlite:///order.db")


@r.post(
    "/orders",
    status_code=status.HTTP_201_CREATED,
    response_model=OrderSchema,
)
def create_order(order: dict) -> OrderSchema:
    with StorageContextManager(database_connexion=DATABASE_CONNEXION) as unit_of_work:
        repo = OrderRepository(unit_of_work.session)
        orders_service = OrderService(repo)
        items = order["items"]
        order = orders_service.create_order(items)
        unit_of_work.commit()
        return_payload = order.dict()
    return return_payload


@r.get("/orders/{order_id}",
       status_code=status.HTTP_200_OK,
       response_model=OrderSchema)
def get_order(order_id: str):
    try:
        with StorageContextManager(database_connexion=DATABASE_CONNEXION) as unit_of_work:
            repo = OrderRepository(unit_of_work.session)
            orders_service = OrderService(repo)
            order = orders_service.get_order(order_id=order_id)
        return order.dict()
    except OrderNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID {order_id} not found"
        )


@r.put(
    "/orders",
    status_code=status.HTTP_205_RESET_CONTENT,
    response_model=OrderSchema,
)
def replace_order(order_details: dict):
    try:
        with StorageContextManager(database_connexion=DATABASE_CONNEXION) as unit_of_work:
            repo = OrderRepository(unit_of_work.session)
            orders_service = OrderService(repo)
            order_id = order_details["id"]
            order = orders_service.replace_order(order_id, order_details)
            unit_of_work.commit()
        return order.dict()
    except OrderNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID {order_id} not found"
        )


@r.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: str):
    try:
        with StorageContextManager(database_connexion=DATABASE_CONNEXION) as unit_of_work:
            repo = OrderRepository(unit_of_work.session)
            orders_service = OrderService(repo)
            orders_service.delete_order(order_id=order_id)
            unit_of_work.commit()
        return {"message": f"Order with ID {order_id} is deleted"}
    except OrderNotFoundError:
        raise HTTPException(
            status_code=404, detail=f"Order with ID {order_id} not found"
        )


@r.get("/orders",
       status_code=status.HTTP_200_OK,
       response_model=List[OrderSchema])
def get_orders(limit: Union[int, None] = None):
    with StorageContextManager(database_connexion=DATABASE_CONNEXION) as unit_of_work:
        repo = OrderRepository(unit_of_work.session)
        orders_service = OrderService(repo)
        results = orders_service.list_orders(limit=limit)
    return [result.dict() for result in results]


@r.get("/health",
       status_code=status.HTTP_200_OK)
def health():
    return {"status": "alive"}
