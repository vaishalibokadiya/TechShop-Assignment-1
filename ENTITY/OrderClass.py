import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')

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
