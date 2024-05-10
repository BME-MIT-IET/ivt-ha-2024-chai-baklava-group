import unittest

import sys 
sys.path.insert(1, '../')

from algorithms.linkedlist.remove_range import Node, remove_range

class TestRemoveRange(unittest.TestCase):

    def test_remove_range(self):
        # Create a linked list: 8 -> 13 -> 17 -> 4 -> 9 -> 12 -> 98 -> 41 -> 7 -> 23 -> 0 -> 92
        head = Node(8)
        current = head
        for val in [13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]:
            current.next = Node(val)
            current = current.next

        # Remove range from index 3 to 8
        remove_range(head, 3, 8)

        # Check if range is removed correctly
        # Expected output: 8 -> 13 -> 17 -> 23 -> 0 -> 92
        expected_output = [8, 13, 17, 23, 0, 92]
        current = head
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

if __name__ == '__main__':
    unittest.main()
