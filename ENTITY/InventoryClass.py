import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')

from Util import DBPropertyUtil, DBConnUtil

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
