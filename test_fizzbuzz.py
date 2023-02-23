# . Write a “fizzBuzz” method that accepts a number as input and returns it as a String.

# Notes:

# start with the minimal failing solution
# keep the three rules in mind and always write just sufficient enough code
# do not forget to refactor your code after each passing test
# write your assertions relating to the exact requirements
# 2. For multiples of three return “Fizz” instead of the number

# 3. For the multiples of five return “Buzz”

# 4. For numbers that are multiples of both three and five return “FizzBuzz”.


import unittest
from parameterized import parameterized
from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        self.fb = FizzBuzz()

    def test_returns_string(self):
        result = self.fb.fizzbuzz(4)
        self.assertIsInstance(result, str)

    @parameterized.expand([("4"), ("7"), ("11")])
    def test_returns_string_of_given_int(self, x):
        result = self.fb.fizzbuzz(int(x))
        self.assertEqual(result, x)

    @parameterized.expand([("3"), ("21"), ("33")])
    def test_multiple_of_3_returns_fizz(self, x):
        result = self.fb.fizzbuzz(int(x))
        self.assertEqual(result, "Fizz")

    @parameterized.expand([("5"), ("20"), ("50")])
    def test_multiple_of_5_returns_buzz(self, x):
        result = self.fb.fizzbuzz(int(x))
        self.assertEqual(result, "Buzz")

    @parameterized.expand([("15"), ("60"), ("60")])
    def test_multiple_of_3_and_5_returns_fizzbuzz(self, x):
        result = self.fb.fizzbuzz(int(x))
        self.assertEqual(result, "FizzBuzz")