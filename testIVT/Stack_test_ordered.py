import unittest
import sys
import os

import sys

sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported


from algorithms.stack.ordered_stack import OrderedStack

class TestOrderedStack(unittest.TestCase):

    def setUp(self):
        self.stack = OrderedStack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_push_and_peek(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.stack.push(1)
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

    def test_pop(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
        self.stack.push(2)
        self.stack.push(1)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(2)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

    def test_order_maintenance(self):
        elements = [5, 3, 8, 1, 4]
        expected_order = [8, 5, 4, 3, 1]
        for elem in elements:
            self.stack.push(elem)
        result = []
        while not self.stack.is_empty():
            result.append(self.stack.pop())
        self.assertEqual(result, expected_order)

if __name__ == '__main__':
    unittest.main()
