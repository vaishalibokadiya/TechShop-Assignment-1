import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

class UpdateProductCatelog:
    def updateProduct():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            productId = int(input("Enter product id: "))
            name=input("Enter product name")
            description=input("Enter description")
            price =float(input("Enter price"))          
            try:
                mycursor.execute(f"UPDATE Product SET name='{name}', description='{description}', price='{price}' WHERE productId={productId};")
            except:
                print("Failed to update product.")
            else:
                print("Product updated successfully.")
