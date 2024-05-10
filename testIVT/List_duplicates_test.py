import unittest
import sys 
sys.path.insert(1, '../')
from algorithms.linkedlist.remove_duplicates import Node, remove_dups, remove_dups_wthout_set

class TestRemoveDups(unittest.TestCase):

    def test_remove_dups(self):
        # Create a linked list with duplicates: A -> A -> B -> C -> D -> C -> F -> G
        a1 = Node("A")
        a2 = Node("A")
        b = Node("B")
        c1 = Node("C")
        d = Node("D")
        c2 = Node("C")
        f = Node("F")
        g = Node("G")

        a1.next = a2
        a2.next = b
        b.next = c1
        c1.next = d
        d.next = c2
        c2.next = f
        f.next = g

        # Remove duplicates using remove_dups function
        remove_dups(a1)

        # Check if duplicates are removed
        # Expected output: A -> B -> C -> D -> F -> G
        expected_output = ["A", "B", "C", "D", "F", "G"]
        current = a1
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

    def test_remove_dups_without_set(self):
        # Create a linked list with duplicates: A -> A -> B -> C -> D -> C -> F -> G
        a1 = Node("A")
        a2 = Node("A")
        b = Node("B")
        c1 = Node("C")
        d = Node("D")
        c2 = Node("C")
        f = Node("F")
        g = Node("G")

        a1.next = a2
        a2.next = b
        b.next = c1
        c1.next = d
        d.next = c2
        c2.next = f
        f.next = g

        # Remove duplicates using remove_dups_without_set function
        remove_dups_wthout_set(a1)

        # Check if duplicates are removed
        # Expected output: A -> B -> C -> D -> F -> G
        expected_output = ["A", "B", "C", "D", "F", "G"]
        current = a1
        for val in expected_output:
            self.assertEqual(current.val, val)
            current = current.next

if __name__ == '__main__':
    unittest.main()
