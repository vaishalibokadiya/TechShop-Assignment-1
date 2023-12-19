class InsufficientStockException:
    def __init__(self, message='Invalid Quantity: Quantity exceeds the available stock'):
        self.message=message