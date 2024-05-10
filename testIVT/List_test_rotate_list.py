import unittest
import sys
import os

# Append the directory above 'tests' to sys.path to find rotate_list module
sys.path.append(os.path.abspath('../'))

from algorithms.linkedlist.rotate_list import ListNode, rotate_right

class TestRotateList(unittest.TestCase):

    def list_to_array(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array

    def array_to_list(self, array):
        if not array:
            return None
        head = ListNode(array[0])
        current = head
        for value in array[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def test_rotate_right(self):
        head = self.array_to_list([1, 2, 3, 4, 5])
        k = 2
        rotated = rotate_right(head, k)
        result = self.list_to_array(rotated)
        self.assertEqual(result, [4, 5, 1, 2, 3])

    def test_empty_list(self):
        head = None
        k = 0
        rotated = rotate_right(head, k)
        self.assertIsNone(rotated)

    def test_k_greater_than_length(self):
        head = self.array_to_list([1, 2, 3])
        k = 4
        rotated = rotate_right(head, k)
        result = self.list_to_array(rotated)
        self.assertEqual(result, [3, 1, 2])

    def test_single_element(self):
        head = self.array_to_list([1])
        k = 0
        rotated = rotate_right(head, k)
        result = self.list_to_array(rotated)
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()
