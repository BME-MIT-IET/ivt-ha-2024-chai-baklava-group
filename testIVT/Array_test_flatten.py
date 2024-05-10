import unittest
import sys

sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

from algorithms.arrays.flatten import flatten, flatten_iter  # Import the flatten function directly

class TestFlattenMethods(unittest.TestCase):

    def test_flatten(self):
        input_arr = [1, [2, 3], [4, [5, 6]], 7]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten(input_arr), expected_output)

        input_arr = [[1, 2, [3]], 4, [5, [6, 7]], 8]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(flatten(input_arr), expected_output)

    def test_flatten_iter(self):
        input_arr = [1, [2, 3], [4, [5, 6]], 7]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(list(flatten_iter(input_arr)), expected_output)

        input_arr = [[1, 2, [3]], 4, [5, [6, 7]], 8]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(list(flatten_iter(input_arr)), expected_output)

if __name__ == 'main':
    print("Testing flatten function")
    unittest.main()