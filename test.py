from main import Cart 
import unittest

class CartTest(unittest.TestCase):
    def test_add_item(self):
        test_add = Cart()
        test_add.add_item('apple','1','6')

        self.assertEqual(len(test_add.items), 1)
    

    def test_item_instantiation(self):
         test_item = item('apple','1','6')

         self.assertEqual(test_item.add,'apple')
         self.assertEqual(test_item.quanity,'1')
         self.assertEqual(test_item.price,'6')
         


    def test_delete_item(self):
        test_add = Cart()
        test_add.add_item('apple','3','15')
        test_add.delete_item('apple')
        self.assertEqual(len(test_add.items),0)


unittest.main()