import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

class Customer:
    def __init__(self, customerId, firstName, lastName, email, phone, address):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.address = address
    
    def set_customerId(self, customerId):
        self.customerId = customerId

    def set_firstName(self, firstName):
        self.firstName = firstName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_address(self, address):
        self.address = address

    def get_customerId(self):
        return self.customerId
    
    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_address(self):
        return self.address
    
    def calculate_total_orders():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter customer Id: "))
            try:
                mycursor.execute(f"SELECT COUNT(*) FROM Order WHERE customerId={customerId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def get_customer_details():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter customer Id: "))
            try:
                mycursor.execute(f"SELECT * FROM Customer WHERE customerId = {customerId};")
            except:
                print("Failed to fetch data from the database.")
            else:
                result=mycursor.fetchall()
                for res in result:
                    print(res)
                print("Data fetched successfully.")

    def update_customer_info():
        try:
            [mycursor,mydb]=DBConnUtil.get_connection_object(DBPropertyUtil.get_connection_string())
        except:
            return "Error in connection"
        else:
            customerId = int(input("Enter ID of the customer you want to update: "))
            firstName = input("Enter first name: ")
            lastName = input("Enter last name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            try: 
                mycursor.execute(f"UPDATE Customer SET firstName='{firstName}',lastName='{lastName}',email='{email}',phone='{phone}',address='{address}' WHERE customerId={customerId};")
            except:
                print("Failed to update customer from the database.")
            else:
                print("Customer updated successfully.")

