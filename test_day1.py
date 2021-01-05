import unittest
from day1 import Palindrom

value1 = Palindrom("Ala ma kota.")
value2 = Palindrom("kalak")
value3 = Palindrom("tasak")
value4 = Palindrom("Cos,co,nie-działa-ale;mogłoby-byc''1")

class TestPalindromsMethods(unittest.TestCase):

    def SetUp(self):
        print('Start')

    def test_format_word(self):
        self.assertEqual(value1.format_word(), 'alamakota')
        self.assertEqual(value2.format_word(), 'kalak')
        self.assertEqual(value3.format_word(), "tasak")
        self.assertEqual(value4.format_word(), "cosconiedziałaalemogłobybyć")

    def test_reverse_word(self):
        self.assertEqual(value1.reverse_word(), 'atokamala')
        self.assertEqual(value2.reverse_word(), 'kalak')
        self.assertEqual(value3.reverse_word(), 'kasat')
        self.assertEqual(value4.reverse_word(), 'cybybołgomelaałaizdeinocsoc')


    def test_is_palindrom(self):
        self.assertFalse(value1.is_palindrom())
        self.assertTrue(value2.is_palindrom())
        self.assertFalse(value3.is_palindrom())
        self.assertFalse(value4.is_palindrom())


if __name__ == '__main__':
    unittest.main()
