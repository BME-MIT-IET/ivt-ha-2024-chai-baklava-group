import unittest
import sys
import os

sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

from algorithms.stack.valid_parenthesis import is_valid

class TestParenthesisValidation(unittest.TestCase):

    def test_valid_parentheses(self):
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        self.assertTrue(is_valid("{[]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(is_valid("(]"))
        self.assertFalse(is_valid("([)]"))
        self.assertFalse(is_valid("(("))
        self.assertFalse(is_valid("{"))
        self.assertFalse(is_valid("}"))
        self.assertFalse(is_valid(")("))

    def test_empty_string(self):
        self.assertTrue(is_valid(""))

if __name__ == '__main__':
    unittest.main()
