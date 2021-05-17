import unittest
from longest_substring import *
import io

class Testword(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(longest_substring(''),0)
        self.assertEqual(longest_substring('a'),1)
        self.assertEqual(longest_substring('aaaa'),1)
        self.assertEqual(longest_substring('↕᭡᭡᭡↕↕᭡↕'),2)
        self.assertEqual(longest_substring('ab'),2)
        self.assertEqual(longest_substring('abc'),3)
        self.assertEqual(longest_substring('abbc'),2)
        self.assertEqual(longest_substring('srescripting'),7)
        self.assertEqual(longest_substring('abc398c03nc-101'),6)
    
unittest.main()