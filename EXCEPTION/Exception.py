class InvalidDataException:
    def __init__(self, message='Data entered is invalid'):
        self.message=message

class InsufficientStockException:
    def __init__(self, message='Invalid Quantity: Quantity exceeds the available stock'):
        self.message=message

class IncompleteOrderException:
    def __init__(self, message='Incomplete order details'):
        self.message=message

class PaymentFailedException:
    def __init__(self, message='Payment failed'):
        self.message=message

class IOException:
    def __init__(self, message='Input/Output error'):
        self.message=message

class SqlException:
    def __init__(self, message='Database Connection failed'):
        self.message=message

class ConcurrencyException:
    def __init__(self, message="Concurrency error"):
        self.message=message

class AuthenticationException:
    def __init__(self, message='Authentication failed'):
        self.message=message