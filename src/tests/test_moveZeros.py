from unittest import TestCase
from src.problems.moveZeros import moveZeros


class TestMoveZeros(TestCase):

    def test_zerosInFront(self):
        result = moveZeros([0, 0, 0, 1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 0, 0, 0])

    def test_zerosInBack(self):
        result = moveZeros([1, 2, 3, 0, 0, 0])
        self.assertEqual(result, [1, 2, 3, 0, 0, 0])

    def test_zerosScattered(self):
        result = moveZeros([0, 1, 0, 2, 0, 3])
        self.assertEqual(result, [1, 2, 3, 0, 0, 0])

    def test_noZeros(self):
        result = moveZeros([1, 2, 3])
        self.assertEqual(result, [1, 2, 3])

    def test_allZeros(self):
        result = moveZeros([0, 0, 0])
        self.assertEqual(result, [0, 0, 0])

    def test_emptyList(self):
        result = moveZeros([])
        self.assertEqual(result, [])
