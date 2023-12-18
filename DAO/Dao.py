import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

class CustomerRegistration:
    def CreateCustomer():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            firstName = input("Enter first name: ")
            lastName=input("Enter last name: ")
            email= input("Enter email")
            phone= input("Enter phone number")
            address= input("Enter address")
            try:
                mycursor.execute(f"INSERT INTO Customer (firstName, lastName, email, phone, address) VALUES ('{firstName}','{lastName}','{email}','{phone}','{address}');")
            except:
                print("Failed to create customer in the database.")
            else:
                print("Customer created successfully.")

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
                mycursor.execute(f"INSERT INTO Order (customerId, orderDate, totalAmount) VALUES ({customerId},'{orderDate}','{totalAmount}');")
            except:
                print("Failed to place order.")
            else:
                print("Order placed successfully.")

class TrackOrderStatus:
    def trackOrderStatus():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            orderId = int(input("Enter order id: "))
            try:
                mycursor.execute(f"SELECT status FROM Order WHERE orderId={orderId};")
            except:
                print("Failed to fetch order status.")
            else:
                print("Order status fetched successfully.")


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

class CustomerAccountUpdate:
    def updateCustomerAccount():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            print("Error in connection")
        else:
            customerId=int(input("Enter customer id"))
            firstName = input("Enter first name: ")
            lastName= input("Enter last name: ")
            email= input("Enter email: ")
            phone=input("Enter phone number: ")
            address=input("Enter address: ")
            try:
                mycursor.execute(f"UPDATE Customer SET firstName='{firstName}', lastName='{lastName}', email='{email}', phone='{phone}', address='{address}' WHERE customerId={customerId};")
            except:
                print("Failed to update customer.")
            else:
                print("Customer Updated successfully.")





