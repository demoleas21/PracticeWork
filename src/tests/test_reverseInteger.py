from unittest import TestCase
from src.problems.reverseInteger import reverse


class ReverseIntegerTests(TestCase):

    def test_reverseSimpleNum(self):
        num = 123
        result = reverse(num)
        self.assertEqual(result, 321)

    def test_reverseNegative(self):
        num = -123
        result = reverse(num)
        self.assertEqual(result, -321)

    def test_reverseZero(self):
        num = 0
        result = reverse(num)
        self.assertEqual(result, 0)

    def test_reverseOverflow(self):
        num = 1123456789
        result = reverse(num)
        self.assertEqual(result, 0)
