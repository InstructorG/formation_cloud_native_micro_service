class OrderItem:
    stock: dict
    def __init__(self, name, quantity, type, stock = None):
        self.name = name
        self.type = type
        self.quantity = quantity
        self.stock = stock


    def add_stock_item(self,stock):
        self.stock = stock

    def dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "quantity": self.quantity,
        }
