import unittest
from reception import Reception
from config import config


class Testing(unittest.TestCase):

    def test_string(self):
        r=Reception([])
        data = r.read_orders(config.filename)
        a = data[0]["id"]
        self.assertEqual(a, "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd")


if __name__ == '__main__':
    unittest.main()