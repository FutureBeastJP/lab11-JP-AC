import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-4, -6), -10)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(4, 10), -6)
        self.assertEqual(sub(0, 0), 0)

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(7, 0), 0)

    def test_divide(self):  # 3 assertions

        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-4, 8), -2)
        self.assertAlmostEqual(div(3, 1), 1 / 3)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions

        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(1, 5), 0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 1)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 2 ** 0.5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=5)
    ##########################


if __name__ == "__main__":
    unittest.main()
