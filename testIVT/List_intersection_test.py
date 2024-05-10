import sys 
sys.path.insert(1, '../')

import unittest

# Assuming the function and class are defined in the linked_list_functions module
from algorithms.linkedlist.intersection import Node, intersection

class TestIntersection(unittest.TestCase):

    def test_intersection(self):
        # Create linked list as:
        # 1 -> 3 -> 5
        #            \
        #             7 -> 9 -> 11
        #            /
        # 2 -> 4 -> 6
        a1 = Node(1)
        b1 = Node(3)
        c1 = Node(5)
        d = Node(7)
        a2 = Node(2)
        b2 = Node(4)
        c2 = Node(6)
        e = Node(9)
        f = Node(11)

        a1.next = b1
        b1.next = c1
        c1.next = d
        a2.next = b2
        b2.next = c2
        c2.next = d
        d.next = e
        e.next = f

        # Test the intersection function
        self.assertEqual(7, intersection(a1, a2).val)

if __name__ == '__main__':
    unittest.main()
