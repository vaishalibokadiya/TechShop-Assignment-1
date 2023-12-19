import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

class PlaceOrder:
    def placeOrder():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            customerId = int(input("Enter customer id: "))
            orderDate=input("Enter order date: ")
            totalAmount= input("Enter total amount")
            try:
                mycursor.execute(f"INSERT INTO Orders (customerId, orderDate, totalAmount) VALUES ({customerId},'{orderDate}','{totalAmount}');")
            except:
                print("Failed to place order.")
            else:
                print("Order placed successfully.")
