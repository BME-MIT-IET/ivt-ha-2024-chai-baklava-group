import unittest
import sys

# Adjust the path to include the directory where longest_non_repeat.py is located.
sys.path.insert(1, '../algorithms/arrays')

# Import the functions directly from the module
from longest_non_repeat import (
    longest_non_repeat_v1,
    longest_non_repeat_v2,
    get_longest_non_repeat_v1,
    get_longest_non_repeat_v2,
    get_longest_non_repeat_v3
)

class TestLongestNonRepeatingSubstring(unittest.TestCase):

    def test_longest_non_repeat_v1_basic(self):
        self.assertEqual(longest_non_repeat_v1("abcabcbb"), 3)
        self.assertEqual(longest_non_repeat_v1("bbbbb"), 1)
        self.assertEqual(longest_non_repeat_v1("pwwkew"), 3)

    def test_longest_non_repeat_v2_basic(self):
        self.assertEqual(longest_non_repeat_v2("abcabcbb"), 3)
        self.assertEqual(longest_non_repeat_v2("bbbbb"), 1)
        self.assertEqual(longest_non_repeat_v2("pwwkew"), 3)

    def test_get_longest_non_repeat_v1_advanced(self):
        self.assertEqual(get_longest_non_repeat_v1("abcabcbb"), (3, "abc"))
        self.assertEqual(get_longest_non_repeat_v1("bbbbb"), (1, "b"))
        self.assertEqual(get_longest_non_repeat_v1("pwwkew"), (3, "wke"))

    def test_get_longest_non_repeat_v2_advanced(self):
        self.assertEqual(get_longest_non_repeat_v2("abcabcbb"), (3, "abc"))
        self.assertEqual(get_longest_non_repeat_v2("bbbbb"), (1, "b"))
        self.assertEqual(get_longest_non_repeat_v2("pwwkew"), (3, "wke"))

    def test_get_longest_non_repeat_v3_advanced(self):
        self.assertEqual(get_longest_non_repeat_v3("abcabcbb"), (3, "abc"))
        self.assertEqual(get_longest_non_repeat_v3("bbbbb"), (1, "b"))
        self.assertEqual(get_longest_non_repeat_v3("pwwkew"), (3, "wke"))

    def test_edge_cases(self):
        self.assertEqual(longest_non_repeat_v1(""), 0)
        self.assertEqual(longest_non_repeat_v2(""), 0)
        self.assertEqual(get_longest_non_repeat_v1(""), (0, ''))
        self.assertEqual(get_longest_non_repeat_v2(""), (0, ''))
        self.assertEqual(get_longest_non_repeat_v3(""), (0, ''))

if __name__ == '__main__':
    unittest.main()
