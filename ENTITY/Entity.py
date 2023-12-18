class Customer:
    def __init__(self, customerId, firstName, lastName, email, phone, address):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.address = address
    
    def set_customerId(self, customerId):
        self.customerId = customerId

    def set_firstName(self, firstName):
        self.firstName = firstName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_address(self, address):
        self.address = address

    def get_customerId(self):
        return self.customerId
    
    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_address(self):
        return self.address
    

class Product:
    def __init__(self, productId, productName, description, price):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price

    def set_productId(self, productId):
        self.productId = productId

    def set_productName(self, productName):
        self.productName = productName

    def set_description(self, description):
        self.description = description

    def set_price(self, price):
        self.price = price

    def get_productId(self):
        return self.productId

    def get_productName(self):
        return self.productName
    
    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    
class Order:
    def __init__(self, orderId, customer, orderDate, totalAmount):
        self.orderId = orderId
        self.customer = customer
        self.orderDate = orderDate
        self.totalAmount = totalAmount

    def set_orderId(self, orderId):
        self.orderId = orderId

    def set_customer(self, customer):
        self.customer = customer

    def set_orderDate(self, orderDate):
        self.orderDate = orderDate

    def set_totalAmount(self, totalAmount):
        self.totalAmount = totalAmount

    def get_orderId(self):
        return self.orderId

    def get_customer(self):
        return self.customer

    def get_orderDate(self):
        return self.orderDate

    def get_totalAmount(self):
        return self.totalAmount

    
class OrderDetails:
    def __init__(self, orderDetailsId, order, product, quantity):
        self.orderDetailsId = orderDetailsId
        self.order = order
        self.product = product
        self.quantity = quantity

    def set_orderDetailsId(self, orderDetailsId):
        self.orderDetailsId = orderDetailsId

    def set_order(self, order):
        self.order = order

    def set_product(self, product):
        self.product = product

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_orderDetailsId(self):
        return self.orderDetailsId

    def get_order(self):
        return self.order

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity


class Inventory:
    def __init__(self, inventoryId, product, quantityInStock, lastStockUpdate):
        self.inventoryId = inventoryId
        self.product = product
        self.quantityInStock = quantityInStock
        self.lastStockUpdate = lastStockUpdate

    def set_inventoryId(self, inventoryId):
        self.inventoryId = inventoryId

    def set_product(self, product):
        self.product = product

    def set_quantityInStock(self, quantityInStock):
        self.quantityInStock = quantityInStock

    def set_lastStockUpdate(self, lastStockUpdate):
        self.lastStockUpdate = lastStockUpdate

    def get_inventoryId(self):
        return self.inventoryId

    def get_product(self):
        return self.product

    def get_quantityInStock(self):
        return self.quantityInStock

    def get_lastStockUpdate(self):
        return self.lastStockUpdate

        