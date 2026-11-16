import unittest
from calculatrice import addition, division


class TestCalculatrice(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

        with self.assertRaises(ValueError):
            division(10, 0)
