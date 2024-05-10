import unittest
import sys
import os

# Adding the project root to the Python path to find the utilities module
sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

from algorithms.stack.simplify_path import simplify_path

class TestPathSimplification(unittest.TestCase):

    def test_simplify_path_basic(self):
        self.assertEqual(simplify_path("/home/"), "/home")
        self.assertEqual(simplify_path("/a/./b/../../c/"), "/c")

    def test_simplify_path_with_multiple_slashes(self):
        self.assertEqual(simplify_path("/home//foo/"), "/home/foo")

    def test_simplify_path_with_dot_and_dotdot(self):
        self.assertEqual(simplify_path("/../"), "/")
        self.assertEqual(simplify_path("/home/./../"), "/")

    def test_simplify_path_empty_and_root(self):
        self.assertEqual(simplify_path(""), "/")
        self.assertEqual(simplify_path("/"), "/")

    def test_simplify_path_complex(self):
        self.assertEqual(simplify_path("/a/./b/./c/./d/"), "/a/b/c/d")
        self.assertEqual(simplify_path("/a/../../././."), "/")

if __name__ == '__main__':
    unittest.main()
