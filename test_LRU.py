import unittest
from LRU import LRU

class TestLRU(unittest.TestCase):


    def test_put(self):
        obj = LRU('a',1)
        self.assertEqual(obj.put('a'),'done')
    def test_get(self):
        obj = LRU('a',1)
        obj.put('a')
        obj.put('b')
        # obj.put('c')
        # print(obj.l)
        self.assertEqual(obj.get(),False)

    def test_get_cache(self):
        obj = LRU('a',1)
        obj.put('a')
        obj.put('b')
        obj.put('c')
        obj.put('d')
        self.assertEqual(obj.get_cache(),['b','c','d'])
if __name__ == '__main__':
    unittest.main()

            