import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/DAO')
from CustomerRegistration import CustomerRegistration
from UpdateProductCatelog import UpdateProductCatelog
from PlaceOrder import PlaceOrder
from TrackOrderStatus import TrackOrderStatus
from InventoryManagement import InventoryManagement
from CustomerAccountUpdate import CustomerAccountUpdate

import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/ENTITY')

from CustomerClass import Customer
from ProductClass import Product
from OrderClass import Order
from OrderDetailsClass import OrderDetails
from InventoryClass import Inventory

def show_menu():
    print("1: Customer Services")
    print("2: Products Services")
    print("3: Orders Services")
    print("4: Order Details Services")
    print("5: Inventory Services")
    choice=int(input("Enter your choice: "))

    if choice==1:
        print("1: Calculate total orders of the customer")
        print("2: Get customer details")
        print("3: Update customer information")
        print("4: Register customer")
        choice2=int(input("Enter your choice: "))
        if choice2==1:
            Customer.calculate_total_orders()
        elif choice2==2:
            Customer.get_customer_details()
        elif choice2==3:
            Customer.update_customer_info()
        elif choice2==4:
            CustomerRegistration.createCustomer()
        else:
            return 

    elif choice==2:
        print("1: Get product details")
        print("2: Update product information")
        choice2=int(input("Enter your choice: "))
        if choice2==1:
            Product.get_product_details()
        elif choice2==2:
            Product.update_product_info()
        else:
            return 

    elif choice==3:
        print("1: Calculate total amount")
        print("2: Get order details")
        print("3: Update order status")
        print("4: Cancel order")
        print("5: Track order status")
        choice2=int(input("Enter your choice: "))
        if choice2==1:
            Order.calculate_total_amount()
        elif choice2==2:
            Order.get_order_details()
        elif choice2==3:
            Order.update_order_status()
        elif choice2==4:
            Order.cancel_order()
        elif choice2==5:
            TrackOrderStatus.trackOrderStatus()
        else:
            return 
        

    elif choice==4:
        print("1: Get order details information")
        print("2: Update quantity")
        print("3: Place order")
        choice2=int(input("Enter your choice: "))
        if choice2==1:
            OrderDetails.get_order_details_info()
        elif choice2==2:
            OrderDetails.update_quantity()
        elif choice2==3:
            PlaceOrder.placeOrder()
        else:
            return 

    elif choice==5:
        print("1: Get product by ID")
        print("2: Get quantity in stock")
        print("3: Update stock quantity")
        print("4: Check if the is product available")
        print("5: List low stock products")
        print("6: List out of stock products")
        print("7: List all products")
        print("8: Add product")
        print("9: Delete product")

        choice2=int(input("Enter your choice: "))
        if choice2==1:
            Inventory.get_product()
        elif choice2==2:
            Inventory.get_quantity_in_stock()
        elif choice2==3:
            Inventory.update_stock_quantity()
        elif choice2==4:
            Inventory.is_product_available()
        elif choice2==5:
            Inventory.list_low_stock_products()
        elif choice2==6:
            Inventory.list_out_of_stock_products()
        elif choice2==7:
            Inventory.list_all_products()
        elif choice2==8:
            InventoryManagement.addProduct()
        elif choice2==9:
            InventoryManagement.deleteProduct()
        else:
            return 

show_menu()

