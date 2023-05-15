import unittest
from StrongPasswordDetection import StrongPasswordDetection

class UnitTests(unittest.TestCase):
    def test_len(self):
        self.assertFalse(StrongPasswordDetection('Test1'))
    def test_number(self):
        self.assertFalse(StrongPasswordDetection("TestWithoutNumber"))
    def test_upperChar(self):
        self.assertFalse(StrongPasswordDetection("testwithoutupper0"))
    def test_lowerChar(self):
        self.assertFalse(StrongPasswordDetection("TESTWITHOUTLOWER0"))

if __name__ == "__main__":
    unittest.main()