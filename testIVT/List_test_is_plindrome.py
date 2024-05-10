import unittest
import sys
import os

sys.path.append(os.path.abspath('../'))

from algorithms.linkedlist.is_palindrome import is_palindrome, is_palindrome_stack, is_palindrome_dict, ListNode

class TestPalindromeList(unittest.TestCase):

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

    def test_palindrome_list(self):
        head = self.array_to_list([1, 2, 2, 1])
        self.assertTrue(is_palindrome(head))
        self.assertTrue(is_palindrome_stack(head))
        self.assertTrue(is_palindrome_dict(head))

    def test_non_palindrome_list(self):
        head = self.array_to_list([1, 2, 3, 4])
        self.assertFalse(is_palindrome(head))
        self.assertFalse(is_palindrome_stack(head))
        self.assertFalse(is_palindrome_dict(head))

    def test_empty_list(self):
        self.assertTrue(is_palindrome(None))
        self.assertTrue(is_palindrome_stack(None))
        self.assertTrue(is_palindrome_dict(None))

    def test_single_element_list(self):
        head = self.array_to_list([1])
        self.assertTrue(is_palindrome(head))
        self.assertTrue(is_palindrome_stack(head))
        self.assertTrue(is_palindrome_dict(head))

    def test_two_element_palindrome_list(self):
        head = self.array_to_list([1, 1])
        self.assertTrue(is_palindrome(head))
        self.assertTrue(is_palindrome_stack(head))
        self.assertTrue(is_palindrome_dict(head))

    def test_two_element_non_palindrome_list(self):
        head = self.array_to_list([1, 2])
        self.assertFalse(is_palindrome(head))
        self.assertFalse(is_palindrome_stack(head))
        self.assertFalse(is_palindrome_dict(head))

if __name__ == '__main__':
    unittest.main()
