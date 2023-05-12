import unittest
from DateDetection import DateDetection

class UnitTests(unittest.TestCase):
    def test_wrong_feb(self):
        self.assertFalse(DateDetection("februrary wrong: 29/02/2023"))
    def test_wrong_smallMonth(self):
        self.assertFalse(DateDetection("April wrong: 31/04/2023"))
    def test_wrong_leapYear(self):
        self.assertFalse(DateDetection("leap year wong: 29/02/2100"))

if __name__ == "__main__":
    unittest.main()