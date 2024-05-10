import unittest
import sys
import os

# Adding the project root to the Python path to find the utilities module
sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

from algorithms.stack.stutter import first_stutter, second_stutter  # Adjust import according to actual file structure

class TestStutter(unittest.TestCase):
    
    def test_first_stutter_basic(self):
        stack = [3, 7, 1, 14, 9]
        expected = [3, 3, 7, 7, 1, 1, 14, 14, 9, 9]
        result = first_stutter(stack.copy())  # Use copy to preserve original stack for other tests
        self.assertEqual(result, expected, "First stutter did not duplicate values correctly.")

    def test_second_stutter_basic(self):
        stack = [3, 7, 1, 14, 9]
        expected = [3, 3, 7, 7, 1, 1, 14, 14, 9, 9]
        result = second_stutter(stack.copy())
        self.assertEqual(result, expected, "Second stutter did not duplicate values correctly.")

    def test_first_stutter_empty(self):
        stack = []
        expected = []
        result = first_stutter(stack)
        self.assertEqual(result, expected, "First stutter did not handle empty stack correctly.")

    def test_second_stutter_empty(self):
        stack = []
        expected = []
        result = second_stutter(stack)
        self.assertEqual(result, expected, "Second stutter did not handle empty stack correctly.")

    def test_first_stutter_single_element(self):
        stack = [5]
        expected = [5, 5]
        result = first_stutter(stack)
        self.assertEqual(result, expected, "First stutter did not duplicate single element correctly.")

    def test_second_stutter_single_element(self):
        stack = [5]
        expected = [5, 5]
        result = second_stutter(stack)
        self.assertEqual(result, expected, "Second stutter did not duplicate single element correctly.")

if __name__ == '__main__':
    unittest.main()
