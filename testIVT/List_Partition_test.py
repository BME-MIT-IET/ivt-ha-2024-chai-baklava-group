

import sys 
sys.path.insert(1, '../')

import unittest
from algorithms.linkedlist.partition import Node, partition

class TestPartition(unittest.TestCase):

    def test_partition(self):
        # Create a linked list: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
        head = Node(3)
        head.next = Node(5)
        head.next.next = Node(8)
        head.next.next.next = Node(5)
        head.next.next.next.next = Node(10)
        head.next.next.next.next.next = Node(2)
        head.next.next.next.next.next.next = Node(1)

        # Perform partition around value 5
        partition(head, 5)

        # Check if partitioning is done correctly
        # Expected output: 3 -> 2 -> 1 -> 5 -> 5 -> 8 -> 10
        expected_output = [3, 2, 1, 5, 5, 8, 10]
        current = head
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

if __name__ == '__main__':
    unittest.main()
