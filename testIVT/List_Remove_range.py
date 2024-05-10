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

    def test_remove_range_single_node(self):
        # Create a linked list with a single node
        head = Node(5)

        # Try to remove a range (should not change the list)
        remove_range(head, 0, 0)

        # Check if list remains unchanged
        self.assertEqual(head.val, 5)
        self.assertIsNone(head.next)

    def test_remove_range_invalid_range(self):
        # Create a linked list: 8 -> 13 -> 17 -> 4 -> 9 -> 12 -> 98 -> 41 -> 7 -> 23 -> 0 -> 92
        head = Node(8)
        current = head
        for val in [13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]:
            current.next = Node(val)
            current = current.next

        # Try to remove an invalid range (start index > end index)
        with self.assertRaises(AssertionError):
            remove_range(head, 5, 3)

        # Check if list remains unchanged
        expected_output = [8, 13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]
        current = head
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

    def test_remove_range_invalid_index(self):
        # Create a linked list: 8 -> 13 -> 17 -> 4 -> 9 -> 12 -> 98 -> 41 -> 7 -> 23 -> 0 -> 92
        head = Node(8)
        current = head
        for val in [13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]:
            current.next = Node(val)
            current = current.next

        # Try to remove range with invalid start index
        with self.assertRaises(IndexError):
            remove_range(head, 12, 15)

        # Try to remove range with invalid end index
        with self.assertRaises(IndexError):
            remove_range(head, 3, 15)

        # Check if list remains unchanged
        expected_output = [8, 13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]
        current = head
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

if __name__ == '__main__':
    unittest.main()
