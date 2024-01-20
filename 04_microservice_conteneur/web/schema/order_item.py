

from pydantic import BaseModel,  validator



class OrderItem(BaseModel):
    id: str
    name: str
    price: int
    quantity: int