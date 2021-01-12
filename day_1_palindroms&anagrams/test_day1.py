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
        cases = [
            (self.value1, 'alamakota'),
            (self.value2, 'kalak'),
            (self.value3, 'tasak'),
            (self.value4, 'cosconiedziałaalemogłobybyc')
        ]
        for value, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(value.format_word(), result)

    def test_reverse_word(self) -> None:
        cases = [
            (self.value1, 'atokamala'),
            (self.value2, 'kalak'),
            (self.value3, 'kasat'),
            (self.value4, 'cybybołgomelaałaizdeinocsoc')
        ]
        for value, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(value.reverse_word(), result)

    def test_is_palindrom(self) ->None:
        self.assertFalse(self.value1.is_palindrom())
        self.assertTrue(self.value2.is_palindrom())
        self.assertFalse(self.value3.is_palindrom())
        self.assertFalse(self.value4.is_palindrom())

    def tearDown(self):
        print('Test finished...')


if __name__ == '__main__':
    unittest.main()
