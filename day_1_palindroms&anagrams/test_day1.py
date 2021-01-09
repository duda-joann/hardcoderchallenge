import unittest
from .day1 import Palindrom


class TestPalindromsMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value1 = Palindrom("Ala ma kota.")
        cls.value2 = Palindrom("kalak")
        cls.value3 = Palindrom("tasak")
        cls.value4 = Palindrom("Cos,co,nie-działa-ale;mogłoby-byc''1")

        print('Start')

    def test_format_word(self) -> None:
        self.assertEqual(self.value1.format_word(), 'alamakota')
        self.assertEqual(self.value2.format_word(), 'kalak')
        self.assertEqual(self.value3.format_word(), "tasak")
        self.assertEqual(self.value4.format_word(), "cosconiedziałaalemogłobybyc")

    def test_reverse_word(self) -> None:
        self.assertEqual(self.value1.reverse_word(), 'atokamala')
        self.assertEqual(self.value2.reverse_word(), 'kalak')
        self.assertEqual(self.value3.reverse_word(), 'kasat')
        self.assertEqual(self.value4.reverse_word(), 'cybybołgomelaałaizdeinocsoc')

    def test_is_palindrom(self) ->None:
        self.assertFalse(self.value1.is_palindrom())
        self.assertTrue(self.value2.is_palindrom())
        self.assertFalse(self.value3.is_palindrom())
        self.assertFalse(self.value4.is_palindrom())

    def tearDown(self):
        print('Test finished...')


if __name__ == '__main__':
    unittest.main()
