import sys 
sys.path.insert(1, '../')

import unittest

# Assuming the function and class are defined in the linked_list_functions module
from algorithms.linkedlist.is_sorted import ListNode, is_sorted

class TestIsSorted(unittest.TestCase):

    def test_is_sorted(self):
        # Test an empty list
        self.assertTrue(is_sorted(None))

        # Test a sorted list: 1 -> 2 -> 3 -> 4
        head1 = ListNode(1)
        head1.next = ListNode(2)
        head1.next.next = ListNode(3)
        head1.next.next.next = ListNode(4)
        self.assertTrue(is_sorted(head1))

        # Test an unsorted list: 1 -> 2 -> -1 -> 3
        head2 = ListNode(1)
        head2.next = ListNode(2)
        head2.next.next = ListNode(-1)
        head2.next.next.next = ListNode(3)
        self.assertFalse(is_sorted(head2))

if __name__ == '__main__':
    unittest.main()
