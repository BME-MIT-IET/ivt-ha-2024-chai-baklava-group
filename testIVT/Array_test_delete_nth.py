import unittest
import sys

sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

from algorithms.arrays.delete_nth import delete_nth, delete_nth_naive  # Import the delete_nth, delete_nth_naive function directly

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
        
    def test_delete_nth_naive(self):
        array = [1, 2, 3, 1, 2, 1, 2, 3]
        n = 2
        expected_result = [1, 2, 3, 1, 2, 3]
        self.assertEqual(delete_nth_naive(array, n), expected_result)

    def test_delete_nth_naive_empty_array(self):
        array = []
        n = 3
        expected_result = []
        self.assertEqual(delete_nth_naive(array, n), expected_result)

    def test_delete_nth_naive_all_elements_repeated(self):
        array = [1, 1, 1, 1, 1]
        n = 2
        expected_result = [1, 1]
        self.assertEqual(delete_nth_naive(array, n), expected_result)

    def test_delete_nth_naive_single_element(self):
        array = [1]
        n = 2
        expected_result = [1]
        self.assertEqual(delete_nth_naive(array, n), expected_result)

    def test_delete_nth_naive_large_input(self):
        array = [1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5]
        n = 2
        expected_result = [1, 2, 3, 4, 4, 5, 5]
        self.assertEqual(delete_nth_naive(array, n), expected_result)

if __name__ == '__main__':
    unittest.main()