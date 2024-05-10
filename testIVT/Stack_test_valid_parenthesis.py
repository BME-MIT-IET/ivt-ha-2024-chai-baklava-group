import unittest
import sys
import os

sys.path.append(os.path.abspath('../'))

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
