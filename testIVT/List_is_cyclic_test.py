import sys
import unittest
import os

sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

from algorithms.linkedlist.is_cyclic import Node, is_cyclic

class TestLinkedListCycle(unittest.TestCase):

    def test_no_cycle(self):
        head = Node(1)
        second = Node(2)
        third = Node(3)
        head.next = second
        second.next = third
        self.assertFalse(is_cyclic(head))

    def test_with_cycle(self):
        head = Node(1)
        second = Node(2)
        third = Node(3)
        head.next = second
        second.next = third
        third.next = second  # Creates a cycle
        self.assertTrue(is_cyclic(head))

    def test_empty_list(self):
        self.assertFalse(is_cyclic(None))

    def test_single_element_no_cycle(self):
        head = Node(1)
        self.assertFalse(is_cyclic(head))

    def test_single_element_with_cycle(self):
        head = Node(1)
        head.next = head  # Creates a cycle
        self.assertTrue(is_cyclic(head))

if __name__ == '__main__':
    unittest.main()