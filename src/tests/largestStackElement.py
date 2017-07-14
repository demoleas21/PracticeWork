from unittest import TestCase
from src.problems.largestStackElement import MaxStack


class LargestStackElementTests(TestCase):
    def test_maxStack(self):
        stack = MaxStack()
        stack.push(1)
        stack.push(6)
        stack.push(2)
        stack.push(5)
        result = stack.getMax()
        self.assertEqual(result, 6)
