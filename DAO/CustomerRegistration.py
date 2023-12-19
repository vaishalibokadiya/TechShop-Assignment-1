import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

class CustomerRegistration:
    def createCustomer():
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
