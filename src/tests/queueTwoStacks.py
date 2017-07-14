from unittest import TestCase
from src.problems.queueTwoStacks import QueueTwoStacks


class QueueTwoStacksTests(TestCase):
    def test_queueTwoStacksOneElement(self):
        queue = QueueTwoStacks()
        queue.enqueue(1)
        self.assertEqual(queue.showStacks(), ([1], []))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([], []))

    def test_queueTwoStacksTwoElements(self):
        queue = QueueTwoStacks()
        queue.enqueue(2)
        self.assertEqual(queue.showStacks(), ([2], []))
        queue.enqueue(3)
        self.assertEqual(queue.showStacks(), ([2, 3], []))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([], [3]))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([], []))

    def test_queueTwoStacksEnqueueDequeueMix(self):
        queue = QueueTwoStacks()
        queue.enqueue(4)
        self.assertEqual(queue.showStacks(), ([4], []))
        queue.enqueue(5)
        self.assertEqual(queue.showStacks(), ([4, 5], []))
        queue.enqueue(6)
        self.assertEqual(queue.showStacks(), ([4, 5, 6], []))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([], [6, 5]))
        queue.enqueue(7)
        self.assertEqual(queue.showStacks(), ([7], [6, 5]))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([7], [6]))
        queue.enqueue(8)
        self.assertEqual(queue.showStacks(), ([7, 8], [6]))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([7, 8], []))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([], [8]))
        queue.dequeue()
        self.assertEqual(queue.showStacks(), ([], []))
