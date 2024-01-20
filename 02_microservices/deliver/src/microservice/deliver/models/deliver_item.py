from enum import Enum
from uuid import uuid4


class TransportEnum(Enum):
    camion = "camion"
    bateau = "bateau"
    avion = "avion"


class DeliverItem:
    deliver_id: uuid4()

    def __init__(self, object, transport, deliver_id=uuid4().__str__()):
        self.deliver_id = deliver_id
        self.object = object
        self.transport = TransportEnum(transport)

    def dict(self):
        return {
            "deliver_id": self.deliver_id,
            "object": str(self.object),
            "transport": self.transport,
        }
