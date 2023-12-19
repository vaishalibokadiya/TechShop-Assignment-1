import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/UTIL')
from Util import DBConnUtil,DBPropertyUtil

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
                return False
            else:
                print("Customer Updated successfully.")
                return True





