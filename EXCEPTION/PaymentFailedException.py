class PaymentFailedException:
    def __init__(self, message='Payment failed'):
        self.message=message