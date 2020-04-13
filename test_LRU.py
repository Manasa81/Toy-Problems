import unittest
import LRU

class TestLRU(unittest.TestCase):


    def test_put(self):
        obj = LRU.LRU("web","a",10)
        self.assertEqual(obj.put(10),'done')
    def test_get(self):
        pass
    def test_get_cache:
        pass
if __name__ == '__main__':
    unittest.main()

            