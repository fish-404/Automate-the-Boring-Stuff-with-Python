import unittest
from RegexStrip import RegexStrip

class UnitTests(unittest.TestCase):
    def test_whiteSpace(self):
        string = '   spac ious   '
        actual = RegexStrip(string)
        excepted = string.strip()
        self.assertEqual(actual, excepted)
    
    def test_letters(self):
        string = 'www.example.com'
        regex = 'cmowz.'
        actual = RegexStrip(string, regex)
        excepted = string.strip(regex)
        self.assertEqual(actual, excepted)
    
    def test_letters_special(self):
        string = '#....... Section 3.2.1 Issue #32 .......'
        regex = '.#! '
        actual = RegexStrip(string, regex)
        excepted = string.strip(regex)
        self.assertEqual(actual, excepted)

if __name__ == "__main__":
    unittest.main()