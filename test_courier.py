import unittest
from orders import Order

from mt_list import MTList

from cook import Cook


class Testing(unittest.TestCase):
    def setUp(self):
        self.o = Order({u'id' : u'a8cfcb76-7f24-4420-a5ba-d46dd77bdffd' , u'prepTime' : 4 , u'name' : u'Banana Split'})
        cooking = MTList()
        cooking.put(self.o)
        self.c = Cook(MTList() , cooking)

    def test_cook_order(self):
        self.c.cook_order()
        self.assertEqual(self.o,self.c.get_delivery_queue().get())

    def test_get_order(self):
        self.assertIsInstance(self.c.get_order(),Order)

if __name__ == '__main__':
    unittest.main()