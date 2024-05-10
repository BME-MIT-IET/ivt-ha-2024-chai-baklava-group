import unittest
import sys
import os

sys.path.append(os.path.abspath('../'))

from algorithms.linkedlist.merge_two_list import Node, merge_two_list, merge_two_list_recur

class TestMergeLists(unittest.TestCase):

    def list_to_array(self, head):
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array

    def array_to_list(self, array):
        if not array:
            return None
        head = Node(array[0])
        current = head
        for value in array[1:]:
            current.next = Node(value)
            current = current.next
        return head

    def test_merge_lists(self):
        l1 = self.array_to_list([1, 2, 4])
        l2 = self.array_to_list([1, 3, 4])
        merged = merge_two_list(l1, l2)
        result = self.list_to_array(merged)
        self.assertEqual(result, [1, 1, 2, 3, 4, 4])

    def test_merge_lists_recursive(self):
        l1 = self.array_to_list([1, 2, 4])
        l2 = self.array_to_list([1, 3, 4])
        merged = merge_two_list_recur(l1, l2)
        result = self.list_to_array(merged)
        self.assertEqual(result, [1, 1, 2, 3, 4, 4])

    def test_empty_list(self):
        l1 = self.array_to_list([1, 2, 3])
        l2 = None
        merged = merge_two_list(l1, l2)
        result = self.list_to_array(merged)
        self.assertEqual(result, [1, 2, 3])
        merged_recur = merge_two_list_recur(l1, None)
        result_recur = self.list_to_array(merged_recur)
        self.assertEqual(result_recur, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
