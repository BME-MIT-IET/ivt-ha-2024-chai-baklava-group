import unittest
import sys
import os

sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

from algorithms.stack.is_sorted import is_sorted

class TestCheckOrder(unittest.TestCase):

    def test_sorted_stack(self):
        stack = [1, 2, 3, 4, 5, 6]
        self.assertTrue(is_sorted(stack))

    def test_unsorted_stack(self):
        stack = [6, 3, 5, 1, 2, 4]
        self.assertFalse(is_sorted(stack))

    def test_empty_stack(self):
        stack = []
        self.assertTrue(is_sorted(stack))  # An empty stack is trivially sorted

    def test_single_element_stack(self):
        stack = [1]
        self.assertTrue(is_sorted(stack))

    def test_duplicates_sorted_stack(self):
        stack = [1, 1, 2, 2, 3, 3]
        self.assertTrue(is_sorted(stack))

    def test_duplicates_unsorted_stack(self):
        stack = [3, 3, 2, 1, 1, 2]
        self.assertFalse(is_sorted(stack))

if __name__ == '__main__':
    unittest.main()
