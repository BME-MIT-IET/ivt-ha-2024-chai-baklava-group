import unittest
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../')

import algorithms.arrays.flatten as ft

class TestFlattenMethods(unittest.TestCase):

    def test_flatten(self):
        input_arr = [1, [2, 3], [4, [5, 6]], 7]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(ft.flatten(input_arr), expected_output)

        input_arr = [[1, 2, [3]], 4, [5, [6, 7]], 8]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(ft.flatten(input_arr), expected_output)

    def test_flatten_iter(self):
        input_arr = [1, [2, 3], [4, [5, 6]], 7]
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(list(ft.flatten_iter(input_arr)), expected_output)

        input_arr = [[1, 2, [3]], 4, [5, [6, 7]], 8]
        expected_output = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(list(flatten.flatten_iter(input_arr)), expected_output)

if __name__ == 'main':
    print("Testing flatten function")
    unittest.main()