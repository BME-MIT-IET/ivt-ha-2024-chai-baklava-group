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

if __name__ == '__main__':
    unittest.main()
