import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
    
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
