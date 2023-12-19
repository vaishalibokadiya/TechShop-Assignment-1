import unittest

import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/TechShop/DAO')

from CustomerAccountUpdate import CustomerAccountUpdate
from InventoryManagement import InventoryManagement

class myTestCase(unittest.TestCase):
    def testAddProduct(self):
        isAdded=InventoryManagement.addProduct()
        self.assertTrue(isAdded)

    def testCustomerUpdate(self):
        isUpdated=CustomerAccountUpdate.updateCustomerAccount()

        self.assertTrue(isUpdated)


if __name__ =="__main__":
    unittest.main()