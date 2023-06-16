import unittest
from replace import replaceAwithB

class UnitTests(unittest.TestCase):
    def test_replaceAwithB(self):
        string = "The ADJECTIVE panda is ADJECTIVE"
        a = "ADJECTIVE"
        b = "cool"
        excepted = "The cool panda is ADJECTIVE"
        actual = replaceAwithB(string, a, b)
        self.assertEqual(actual, excepted)

if __name__ == "__main__":
    unittest.main()
