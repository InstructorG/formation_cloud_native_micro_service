from uuid import uuid4


class Bill:

    def __init__(self, object_details, bill_id=uuid4().__str__()):
        self.bill_id = bill_id
        self.object_details = object_details

    def dict(self):
        return {
            "bill_id": self.bill_id,
            "object_details": str(self.object_details)
        }
