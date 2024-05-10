import unittest
import sys 
sys.path.insert(1, '../')
from algorithms.linkedlist.swap_in_pairs import Node, swap_pairs

class TestSwapPairs(unittest.TestCase):

    def test_swap_pairs(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)

        # Swap every two adjacent nodes
        head = swap_pairs(head)

        # Check if nodes are swapped correctly
        # Expected output: 2 -> 1 -> 4 -> 3
        expected_output = [2, 1, 4, 3]
        current = head
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

    def test_swap_pairs_empty_list(self):
        # Test swapping in an empty list
        head = None
        head = swap_pairs(head)
        self.assertIsNone(head)

    def test_swap_pairs_single_node(self):
        # Test swapping in a list with a single node
        head = Node(1)
        head = swap_pairs(head)
        self.assertEqual(head.val, 1)
        self.assertIsNone(head.next)

    def test_swap_pairs_odd_length_list(self):
        # Create a linked list with odd length: 1 -> 2 -> 3 -> 4 -> 5
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)

        # Swap every two adjacent nodes
        head = swap_pairs(head)

        # Check if nodes are swapped correctly
        # Expected output: 2 -> 1 -> 4 -> 3 -> 5
        expected_output = [2, 1, 4, 3, 5]
        current = head
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

    def test_swap_pairs_even_length_list(self):
        # Create a linked list with even length: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)

        # Swap every two adjacent nodes
        head = swap_pairs(head)

        # Check if nodes are swapped correctly
        # Expected output: 2 -> 1 -> 4 -> 3 -> 6 -> 5
        expected_output = [2, 1, 4, 3, 6, 5]
        current = head
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

if __name__ == '__main__':
    unittest.main()
