import unittest
import sys

# Adjust the path to include the directory where delete_nth.py is located.
# Assuming your test folder is at the same level as the algorithms folder.
sys.path.insert(1, '../algorithms/arrays')

from delete_nth import delete_nth  # Import the delete_nth function directly

class TestDeleteNth(unittest.TestCase):

    def test_delete_nth(self):
        array = [1, 2, 3, 1, 2, 1, 2, 3]
        n = 2
        expected_result = [1, 2, 3, 1, 2, 3]
        self.assertEqual(delete_nth(array, n), expected_result)

    def test_delete_nth_empty_array(self):
        array = []
        n = 3
        expected_result = []
        self.assertEqual(delete_nth(array, n), expected_result)

    def test_delete_nth_all_elements_repeated(self):
        array = [1, 1, 1, 1, 1]
        n = 2
        expected_result = [1, 1]
        self.assertEqual(delete_nth(array, n), expected_result)

    def test_delete_nth_single_element(self):
        array = [1]
        n = 2
        expected_result = [1]
        self.assertEqual(delete_nth(array, n), expected_result)

    def test_delete_nth_large_input(self):
        array = [1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5]
        n = 2
        expected_result = [1, 2, 3, 4, 4, 5, 5]
        self.assertEqual(delete_nth(array, n), expected_result)

if __name__ == '__main__':
    unittest.main()

