import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/DAO')
from DAO import CustomerRegistration, UpdateProductCatelog, PlaceOrder, TrackOrderStatus, InventoryManagement, CustomerAccountUpdate

CustomerRegistration.CreateCustomer()
CustomerAccountUpdate.updateCustomerAccount()
PlaceOrder.placeOrder()
TrackOrderStatus.trackOrderStatus()
InventoryManagement.addProduct()
InventoryManagement.updateProduct()
InventoryManagement.deleteProduct()
UpdateProductCatelog.updateProduct()

