class StockItem:
    name: str
    type: str
    quantity: int
    price: float

    def __init__(self, name, type, quantity, price):
        self.name = name
        self.type = type
        self.quantity = quantity
        self.price = price

    def dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'price': self.price,
            'quantity': self.quantity
        }