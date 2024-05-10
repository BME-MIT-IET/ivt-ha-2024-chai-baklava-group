import unittest
import sys
import os

# Adjust the path to ensure the 'remove_min' function can be imported correctly
sys.path.insert(1, '../')  # Including the parent directory to the path

from algorithms.stack.remove_min import remove_min

class TestRemoveMin(unittest.TestCase):

    def test_remove_min_basic(self):
        stack = [2, 8, 3, -6, 7, 3]
        expected = [2, 8, 3, 7, 3]
        result = remove_min(stack)
        self.assertEqual(result, expected, "Failed to remove the smallest element correctly.")

    def test_remove_min_with_duplicates(self):
        stack = [2, 1, 3, 1, 7, 3, 1]
        expected = [2, 3, 1, 7, 3, 1]  # Only the first '1' is removed
        result = remove_min(stack)
        self.assertEqual(result, expected, "Failed to remove only the first occurrence of the minimum value.")

    def test_empty_stack(self):
        stack = []
        expected = []
        result = remove_min(stack)
        self.assertEqual(result, expected, "Should return an empty stack if input stack is empty.")

    def test_single_element(self):
        stack = [10]
        expected = []
        result = remove_min(stack)
        self.assertEqual(result, expected, "Should remove the single element, resulting in an empty stack.")

    def test_remove_min_all_same(self):
        stack = [4, 4, 4, 4]
        expected = [4, 4, 4]  # One '4' is removed
        result = remove_min(stack)
        self.assertEqual(result, expected, "Should remove only one instance of the same element.")

    # New Tests
    def test_remove_min_negative_numbers(self):
        stack = [-1, -3, -2, -5, -4]
        expected = [-1, -3, -2, -4]  # Remove the smallest, which is -5
        result = remove_min(stack)
        self.assertEqual(result, expected, "Failed to correctly remove the smallest negative number.")

    def test_remove_min_increasing_order(self):
        stack = [1, 2, 3, 4, 5]
        expected = [2, 3, 4, 5]  # Remove the smallest at the bottom
        result = remove_min(stack)
        self.assertEqual(result, expected, "Failed to correctly remove the smallest number in an increasing order stack.")

    def test_remove_min_decreasing_order(self):
        stack = [5, 4, 3, 2, 1]
        expected = [5, 4, 3, 2]  # Remove the smallest at the top
        result = remove_min(stack)
        self.assertEqual(result, expected, "Failed to correctly remove the smallest number in a decreasing order stack.")

    def test_remove_min_with_zero(self):
        stack = [0, 2, 3, 0, 4]
        expected = [2, 3, 0, 4]  # Remove the first zero
        result = remove_min(stack)
        self.assertEqual(result, expected, "Failed to correctly remove the first zero.")

if __name__ == '__main__':
    unittest.main()
