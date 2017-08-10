from unittest import TestCase
from src.problems.palindromeNumber import isPalindrome


class PalindromeNumberTests(TestCase):

    def test_isPalindrome(self):
        num = 12321
        result = isPalindrome(num)
        self.assertTrue(result)

    def test_isNotPalindrome(self):
        num = 12331
        result = isPalindrome(num)
        self.assertFalse(result)

    def test_isPalindromeSingle(self):
        num = 1
        result = isPalindrome(num)
        self.assertTrue(result)
