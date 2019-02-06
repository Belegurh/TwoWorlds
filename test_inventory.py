# This script tests the funcions append_item and remove_item from the module inventory.

import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):

    def setUp(self):
        self.bag = Inventory(["pen", "sandwich", "penny", "bottle"], 10)
        self.bag_new = Inventory([], 10)

    def tearDown(self):
        pass

    def test_append_item(self):
        self.bag.append_item("branch")
        self.bag_new.append_item("branch")

        self.assertEqual(self.bag.list, ["pen", "sandwich", "penny", "bottle", "branch"])
        self.assertEqual(self.bag_new.list, ["branch"])

    def test_remove_item(self):
        self.bag.remove_item("penny")

        self.bag_new.append_item("shirt")
        self.bag_new.append_item("helmet")
        self.bag_new.remove_item("shirt")

        self.assertEqual(self.bag.list, ["pen", "sandwich", "bottle"])
        self.assertEqual(self.bag_new.list, ["helmet"])


if __name__ == '__main__':
    unittest.main()