import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

class InventoryManagement:
    def addProduct():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            name=input("Enter product name")
            description=("Enter description")
            price=("Enter price")
            try:
                mycursor.execute(f"INSERT INTO Product (name, description, price) VALUES ('{name}','{description}',{price});")
            except:
                print("Failed to add product in the database.")
            else:
                print("Product added successfully.")

    def updateQuantity():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            orderDetailsId = int(input("Enter order details Id: "))
            quantity= input("Enter updated quantity")
            try:
                mycursor.execute(f"UPDATE Inventory SET quantity={quantity} WHERE orderDetailsId = {orderDetailsId};")
            except:
                print("Failed to update quantity in the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("quantity updated successfully.")

    def deleteProduct():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            productId = int(input("Enter product Id: "))
            try:
                mycursor.execute(f"DELETE FROM Product WHERE productId = {productId};")
            except:
                print("Failed to delete product from the database.")
            else:
                print("Product deleted successfully.")
