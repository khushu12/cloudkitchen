import unittest
from mt_list import MTList

class Testing(unittest.TestCase):

    def test_put(self):

        mtlist=MTList()
        acha_naam='a'
        mtlist.put(acha_naam)
        self.assertEqual(acha_naam,mtlist.value[0])

    def test_get(self):
        mtlist=MTList()
        acha_naam='a'
        mtlist.put(acha_naam)
        self.assertEqual(acha_naam,mtlist.get())
        self.assertNotIn(acha_naam,mtlist.value)

if __name__ == '__main__':
    unittest.main()