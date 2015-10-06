import unittest
import lib
import math

class LibTest(unittest.TestCase):

    def test_sqrt_non_negative_arg(self):
        self.assertEqual(lib.sqrt(9), 3)
        self.assertEqual(lib.sqrt(1), 1)
        self.assertEqual(lib.sqrt(0), 0)

    def test_sqrt_negative(self):
        self.assertEqual(lib.sqrt(-1), 0)

    def test_even_true(self):
        self.assertEqual(lib.even(2), 1)
        self.assertEqual(lib.even(8), 1)
        self.assertEqual(lib.even(-6), 1)

    def test_even_false(self):
        self.assertEqual(lib.even(5), 0)
        self.assertEqual(lib.even(9), 0)

    def test_factorial_non_negative_arg(self):
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(3), 6)

    def test_factorial_negative_arg(self):
        self.assertEqual(lib.factorial(-1), 1)
        self.assertEqual(lib.factorial(-6), 1)

    def test_palindrome_true(self):
        self.assertEqual(lib.palindrome('121'), 1)
        self.assertEqual(lib.palindrome('abba'), 1)

    def test_palindrome_false(self):
        self.assertEqual(lib.palindrome('llk'), 0)
        self.assertEqual(lib.palindrome('123'), 0)

    def test_prime_true(self):
        self.assertEqual(lib.prime(13), 1)
        self.assertEqual(lib.prime(7), 1)

    def test_prime_false(self):
        self.assertEqual(lib.prime(6), 0)
        self.assertEqual(lib.prime(8), 0)

    def test_sin(self):
        self.assertEqual(lib.sin(math.pi / 6), 0.5)
        self.assertEqual(lib.sin(0), 0)

unittest.main(verbosity=2)
