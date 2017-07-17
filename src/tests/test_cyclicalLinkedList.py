from unittest import TestCase
from src.problems.cyclicalLinkedList import containsCycle
from src.structures import LinkedList


class CyclicalLinkedListTests(TestCase):
    def test_containsCycleTrue(self):
        a = LinkedList('A')
        b = LinkedList('B')
        c = LinkedList('C')
        d = LinkedList('D')
        a.next = b
        b.next = c
        c.next = d
        d.next = b
        result = containsCycle(a)
        self.assertTrue(result)

    def test_containsCycleFalse(self):
        a = LinkedList('A')
        b = LinkedList('B')
        c = LinkedList('C')
        d = LinkedList('D')
        a.next = b
        b.next = c
        c.next = d
        result = containsCycle(a)
        self.assertFalse(result)
