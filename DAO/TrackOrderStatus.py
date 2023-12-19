import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

class TrackOrderStatus:
    def trackOrderStatus():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            orderId = int(input("Enter order id: "))
            try:
                mycursor.execute(f"SELECT status FROM Orders WHERE orderId={orderId};")
            except:
                print("Failed to fetch order status.")
            else:
                print("Order status fetched successfully.")
