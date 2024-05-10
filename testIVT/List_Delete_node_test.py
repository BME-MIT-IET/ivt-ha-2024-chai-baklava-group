import unittest
import sys 
sys.path.insert(1, '../')

from algorithms.linkedlist.delete_node import Node, delete_node

class TestDeleteNode(unittest.TestCase):

    def test_delete_node(self):
        # Make linked list: 1 -> 2 -> 3 -> 4
        head = Node(1)
        curr = head
        for i in range(2, 6):
            curr.next = Node(i)
            curr = curr.next

        # Node to delete: node3 = 3
        node3 = head.next.next

        # After delete_node: 1 -> 2 -> 4
        delete_node(node3)

        # Assert statements
        curr = head
        self.assertEqual(1, curr.val)

        curr = curr.next
        self.assertEqual(2, curr.val)

        curr = curr.next
        self.assertEqual(4, curr.val)

        curr = curr.next
        self.assertEqual(5, curr.val)

        tail = curr
        self.assertIsNone(tail.next)

        # Test deleting tail node
        self.assertRaises(ValueError, delete_node, tail)
        self.assertRaises(ValueError, delete_node, tail.next)

if __name__ == '__main__':
    unittest.main()
