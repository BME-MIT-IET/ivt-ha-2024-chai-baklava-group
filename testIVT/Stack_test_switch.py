import unittest
import sys
import os

sys.path.insert(1, '../')  # Including the parent directory to the path so that the module can be imported

from algorithms.stack.switch_pairs import first_switch_pairs, second_switch_pairs

class TestSwitchPairs(unittest.TestCase):

    def test_first_switch_pairs_even(self):
        stack = [3, 8, 17, 9, 1, 10]
        expected = [8, 3, 9, 17, 10, 1]
        result = first_switch_pairs(stack.copy())
        self.assertEqual(result, expected)

    def test_first_switch_pairs_odd(self):
        stack = [3, 8, 17, 9, 1]
        expected = [8, 3, 9, 17, 1]
        result = first_switch_pairs(stack.copy())
        self.assertEqual(result, expected)

    def test_second_switch_pairs_even(self):
        stack = [3, 8, 17, 9, 1, 10]
        expected = [8, 3, 9, 17, 10, 1]
        result = second_switch_pairs(stack.copy())
        self.assertEqual(result, expected)

    def test_second_switch_pairs_odd(self):
        stack = [3, 8, 17, 9, 1]
        expected = [8, 3, 9, 17, 1]
        result = second_switch_pairs(stack.copy())
        self.assertEqual(result, expected)

    def test_first_switch_pairs_empty(self):
        stack = []
        expected = []
        result = first_switch_pairs(stack)
        self.assertEqual(result, expected)

    def test_second_switch_pairs_empty(self):
        stack = []
        expected = []
        result = second_switch_pairs(stack)
        self.assertEqual(result, expected)

    def test_first_switch_pairs_single_element(self):
        stack = [3]
        expected = [3]
        result = first_switch_pairs(stack)
        self.assertEqual(result, expected)

    def test_second_switch_pairs_single_element(self):
        stack = [3]
        expected = [3]
        result = second_switch_pairs(stack)
        self.assertEqual(result, expected)

    # New Tests
    def test_with_repeating_elements(self):
        stack = [5, 5, 5, 5]
        expected = [5, 5, 5, 5]
        result = first_switch_pairs(stack.copy())
        self.assertEqual(result, expected)
        result = second_switch_pairs(stack.copy())
        self.assertEqual(result, expected)

    def test_with_alternating_pattern(self):
        stack = [1, 2, 1, 2, 1, 2]
        expected = [2, 1, 2, 1, 2, 1]
        result = first_switch_pairs(stack.copy())
        self.assertEqual(result, expected)
        result = second_switch_pairs(stack.copy())
        self.assertEqual(result, expected)

    def test_with_decimals_and_negatives(self):
        stack = [1.5, -1.5, 3.5, -3.5]
        expected = [-1.5, 1.5, -3.5, 3.5]
        result = first_switch_pairs(stack.copy())
        self.assertEqual(result, expected)
        result = second_switch_pairs(stack.copy())
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
