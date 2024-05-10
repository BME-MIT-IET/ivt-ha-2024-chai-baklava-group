import unittest
import sys
import os

# Adjust the path so that the module can be imported correctly
sys.path.insert(1, '../')  # Including the parent directory to the path

from algorithms.stack.is_consecutive import first_is_consecutive, second_is_consecutive

class TestConsecutiveCheck(unittest.TestCase):

    def test_first_is_consecutive_true(self):
        stack = [3, 4, 5, 6, 7]
        self.assertTrue(first_is_consecutive(stack.copy()))

    def test_first_is_consecutive_false(self):
        stack = [3, 4, 6, 7]
        self.assertFalse(first_is_consecutive(stack.copy()))

    def test_first_is_consecutive_reverse_order(self):
        stack = [3, 2, 1]
        self.assertFalse(first_is_consecutive(stack.copy()))

    def test_second_is_consecutive_true(self):
        stack = [3, 4, 5, 6, 7]
        self.assertTrue(second_is_consecutive(stack.copy()))

    def test_second_is_consecutive_false(self):
        stack = [3, 4, 6, 7]
        self.assertFalse(second_is_consecutive(stack.copy()))

    def test_second_is_consecutive_reverse_order(self):
        stack = [3, 2, 1]
        self.assertFalse(second_is_consecutive(stack.copy()))

    def test_empty_stack(self):
        stack = []
        self.assertTrue(first_is_consecutive(stack.copy()))
        self.assertTrue(second_is_consecutive(stack.copy()))

    def test_single_element_stack(self):
        stack = [1]
        self.assertTrue(first_is_consecutive(stack.copy()))
        self.assertTrue(second_is_consecutive(stack.copy()))

    # New tests
    def test_with_repeated_elements(self):
        stack = [1, 1, 2, 2, 3, 3]
        self.assertFalse(first_is_consecutive(stack.copy()))
        self.assertFalse(second_is_consecutive(stack.copy()))

    def test_with_large_range(self):
        stack = list(range(100))  # 0 to 99
        self.assertTrue(first_is_consecutive(stack.copy()))
        self.assertTrue(second_is_consecutive(stack.copy()))

    def test_with_non_consecutive_large_range(self):
        stack = list(range(0, 100, 2))  # 0, 2, 4, ..., 98
        self.assertFalse(first_is_consecutive(stack.copy()))
        self.assertFalse(second_is_consecutive(stack.copy()))

    def test_with_mix_of_consecutive_and_non_consecutive(self):
        stack = [1, 2, 3, 5, 6, 7, 9]
        self.assertFalse(first_is_consecutive(stack.copy()))
        self.assertFalse(second_is_consecutive(stack.copy()))

    def test_alternating_consecutive(self):
        stack = [1, 1, 2, 3, 4, 4]
        self.assertFalse(first_is_consecutive(stack.copy()))
        self.assertFalse(second_is_consecutive(stack.copy()))

if __name__ == '__main__':
    unittest.main()
