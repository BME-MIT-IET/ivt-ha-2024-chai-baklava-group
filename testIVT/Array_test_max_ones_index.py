import unittest
import sys

# Adjust the path to include the directory where max_ones_index.py is located.
sys.path.insert(1, '../algorithms/arrays')

# Import the max_ones_index function from the module
from max_ones_index import max_ones_index

class TestMaxOnesIndex(unittest.TestCase):

    def test_max_ones_index_basic(self):
        self.assertEqual(max_ones_index([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]), 3)
        self.assertEqual(max_ones_index([1, 1, 1, 1, 1, 0, 1]), 5)
        self.assertEqual(max_ones_index([0, 1, 1, 1, 0, 1, 1]), 4)  # Corrected expected index


    def test_max_ones_index_no_zeros(self):
        self.assertEqual(max_ones_index([1, 1, 1, 1]), -1)

    def test_max_ones_index_all_zeros(self):
        self.assertEqual(max_ones_index([0, 0, 0, 0]), 0)

    def test_max_ones_index_single_zero(self):
        self.assertEqual(max_ones_index([0]), 0)

    def test_max_ones_index_edge_cases(self):
        self.assertEqual(max_ones_index([]), -1)  # Empty array
        self.assertEqual(max_ones_index([0]), 0)  # Single element array with zero
        self.assertEqual(max_ones_index([1]), -1)  # Single element array without zero

if __name__ == '__main__':
    unittest.main()
