import unittest
import sys

# Adjust the path for importing based on your file organization
sys.path.insert(1, '../algorithms/arrays')

from limit import limit  # Import the limit function directly

class TestLimit(unittest.TestCase):

    def test_limit_no_min_max(self):
        array = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(limit(array), expected_result)

    def test_limit_with_min(self):
        array = [1, 2, 3, 4, 5]
        min_value = 2
        expected_result = [2, 3, 4, 5]
        self.assertEqual(limit(array, min_lim=min_value), expected_result)

    # Add more tests as needed...

if __name__ == '__main__':
    unittest.main()
