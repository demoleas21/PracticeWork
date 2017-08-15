from unittest import TestCase
from src.problems.fizzBuzz import fizzBuzz


class FizzBuzzTests(TestCase):

    def test_fizzBuzz15(self):
        result = fizzBuzz(15)
        answer = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]
        self.assertEqual(result, answer)

    def test_fizzBuzz10(self):
        result = fizzBuzz(10)
        answer = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz"
        ]
        self.assertEqual(result, answer)

    def test_fizzbuzz5(self):
        result = fizzBuzz(5)
        answer = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz"
        ]
        self.assertEqual(result, answer)

    def test_fizzBuzz0(self):
        result = fizzBuzz(0)
        answer = []
        self.assertEqual(result, answer)
