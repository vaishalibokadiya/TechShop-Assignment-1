import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

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
    
    def calculate_total_orders():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter customer Id: "))
            try:
                mycursor.execute(f"SELECT COUNT(*) FROM Order WHERE customerId={customerId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def get_customer_details():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter customer Id: "))
            try:
                mycursor.execute(f"SELECT * FROM Customer WHERE customerId = {customerId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def update_customer_info():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter ID of the customer you want to update: "))
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            try: 
                mycursor.execute(f"UPDATE Customer SET firstName='{firstName}',lastName='{lastName}',email='{email}',phone='{phone}',address='{address}' WHERE customerId={customerId};")
            except:
                print("Failed to update customer from the database.")
            else:
                print("Customer updated successfully.")


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
    
    def get_product_details():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            productId = int(input("Enter product Id: "))
            try:
                mycursor.execute(f"SELECT * FROM Product WHERE productId = {productId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def update_product_info():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            productId = int(input("Enter ID of the product you want to update: "))
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter price: "))
            try: 
                mycursor.execute(f"UPDATE Product SET name='{name}', description='{description}', price='{price}' WHERE productId={productId};")
            except:
                print("Failed to update product in the database.")
            else:
                print("Product updated successfully.")
    
    
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

    def calculate_total_amount():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            orderId = int(input("Enter order Id: "))
            try:
                mycursor.execute(f"SELECT totalAmount FROM Order WHERE orderId = {orderId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def get_order_details():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            orderId = int(input("Enter order Id: "))
            try:
                mycursor.execute(f"SELECT * FROM Order WHERE orderId = {orderId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def update_order_status():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            orderId = int(input("Enter order Id: "))
            status= input("Enter updated order status")
            try:
                mycursor.execute(f"UPDATE Order SET status='{status}' WHERE orderId = {orderId};")
            except:
                print("Failed to update status in the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Status updated successfully.")

    def cancel_order():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            orderId = int(input("Enter order Id: "))
            try:
                mycursor.execute(f"DELETE FROM Order WHERE orderId = {orderId};")
            except:
                print("Failed to delete data from the database.")
            else:
                print("Data deleted successfully.")

    
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
    
    def get_order_details_info():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            orderDetailsId = int(input("Enter order Id: "))
            try:
                mycursor.execute(f"SELECT * FROM OrderDetails WHERE orderDetailsId = {orderDetailsId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                print("Data fetched successfully.")

    def update_quantity():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            orderDetailsId = int(input("Enter order details Id: "))
            quantity= input("Enter updated quantity")
            try:
                mycursor.execute(f"UPDATE OrderDetails SET quantity={quantity} WHERE orderDetailsId = {orderDetailsId};")
            except:
                print("Failed to update quantity in the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("quantity updated successfully.")

   


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
    
    def get_product():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            productId = int(input("Enter product Id: "))
            try:
                mycursor.execute(f"SELECT * FROM Product WHERE productId = {productId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def get_quantity_in_stock():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            inventoryId = int(input("Enter inventory Id: "))
            try:
                mycursor.execute(f"SELECT quantityInStock FROM Inventory WHERE inventoryId = {inventoryId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def update_stock_quantity():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            inventoryId = int(input("Enter inventory Id: "))
            quantity= int(input("Enter updated quantity"))
            try:
                mycursor.execute(f"UPDATE Inventory SET quantityInStock={quantity} WHERE inventoryId={inventoryId};")
            except:
                print("Failed to update quantity in the database.")
            else:
                print("Quantity updated successfully.")

    def is_product_available():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            productId=int(input("Enter product id"))
            threshold=int(input("Enter quantity"))
            try:
                mycursor.execute(f"SELECT * FROM Inventory WHERE productId={productId} AND quantityInStock>={threshold};")
            except:
                print("Failed to fetch data from the database.")
            else:
                rows=mycursor.fetchall()
                for row in rows:
                    print(row)
                print("Data fetched successfully.")

    def list_low_stock_products():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            threshold=int(input("Enter threshold for low quantity"))
            try:
                mycursor.execute(f"SELECT product, quantityInStock FROM Inventory WHERE quantityInStock<{threshold};")
            except:
                print("Failed to fetch data from the database.")
            else:
                rows=mycursor.fetchall()
                for row in rows:
                    print(row)
                print("Data fetched successfully.")

    def list_out_of_stock_products():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            try:
                mycursor.execute(f"SELECT product, quantityInStock FROM Inventory WHERE quantityInStock=0;")
            except:
                print("Failed to fetch data from the database.")
            else:
                rows=mycursor.fetchall()
                for row in rows:
                    print(row)
                print("Data fetched successfully.")

    def list_all_products():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            try:
                mycursor.execute(f"SELECT product, quantityInStock FROM Inventory;")
            except:
                print("Failed to fetch data from the database.")
            else:
                rows=mycursor.fetchall()
                for row in rows:
                    print(row)
                print("Data fetched successfully.")
