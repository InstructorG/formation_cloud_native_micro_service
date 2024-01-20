from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel,  validator

from web.schema.order_item import OrderItem


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    updated = "updated"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class OrderSchema(BaseModel):
    id: str
    created: Optional[datetime] = datetime.utcnow()
    status: Optional[StatusEnum]
    items: List[OrderItem]

    @validator("id")
    def id_length_sup_3(cls, value):
        assert len(value) > 3, "id must be larger than 3 digits"
        return value