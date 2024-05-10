import unittest
import sys
import os

sys.path.append(os.path.abspath('../'))

from algorithms.linkedlist.reverse import ListNode, reverse_list, reverse_list_recursive

class TestReverseList(unittest.TestCase):

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

    def test_reverse_list(self):
        head = self.array_to_list([1, 2, 3, 4])
        reversed_head = reverse_list(head)
        result = self.list_to_array(reversed_head)
        self.assertEqual(result, [4, 3, 2, 1])

    def test_reverse_list_recursive(self):
        head = self.array_to_list([1, 2, 3, 4])
        reversed_head = reverse_list_recursive(head)
        result = self.list_to_array(reversed_head)
        self.assertEqual(result, [4, 3, 2, 1])

    def test_empty_list(self):
        self.assertIsNone(reverse_list(None))
        self.assertIsNone(reverse_list_recursive(None))

    def test_single_element(self):
        head = self.array_to_list([1])
        reversed_head = reverse_list(head)
        result = self.list_to_array(reversed_head)
        self.assertEqual(result, [1])
        reversed_head_rec = reverse_list_recursive(head)
        result_rec = self.list_to_array(reversed_head_rec)
        self.assertEqual(result_rec, [1])

if __name__ == '__main__':
    unittest.main()
