import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

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
    