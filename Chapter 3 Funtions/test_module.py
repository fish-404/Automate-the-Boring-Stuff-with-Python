import unittest
from CollatzSequence import Collatz

class UnitTests(unittest.TestCase):
    def test_odd(self):
        actual = Collatz(3)
        excepted = 10
        self.assertEqual(actual, excepted, 'Expected calling "Collatz()" with 3, to return 10')
    
    def test_even(self):
        actual = Collatz(10)
        excepted = 5
        self.assertEqual(actual, excepted, 'Expected calling "Collatz()" with 10, to return 5')
    
if __name__ == "__main__":
    unittest.main()
