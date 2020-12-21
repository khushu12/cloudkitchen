import unittest
from reception import Reception
from config import config
from orders import Order
from mt_list import MTList
class Testing(unittest.TestCase):

    def test_string(self):
        r = Reception(MTList())
        data = r.read_orders(config.filename)
        a = data[0]["id"]
        self.assertEqual(a, "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd")

    def test_reception_read_order(self):
        r = Reception(MTList())
        # data = r.read_orders(config.filename)
        result = r.read_orders(config.filename)
        self.assertIsInstance(result , list)

    def test_put_order_to_queue(self):
        r = Reception(MTList())
        data = r.read_orders(config.filename)
        r.put_order_to_queue(data[0])
        self.assertEqual(Order(data[0]).__str__(),r.get_cooking_queue().get().__str__())

    def test_get_cooking_queue(self):
        r = Reception(MTList())
        self.assertIsInstance(r.get_cooking_queue(),MTList)


if __name__ == '__main__':
    unittest.main()