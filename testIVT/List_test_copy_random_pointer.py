import unittest
from collections import defaultdict
import sys 

sys.path.insert(1, '../') # Including the parent directory to the path so that the module can be imported

# Assuming the functions and class are defined in the linked_list_functions module
from algorithms.linkedlist.copy_random_pointer import RandomListNode, copy_random_pointer_v1, copy_random_pointer_v2

class TestCopyRandomPointer(unittest.TestCase):
    def test_copy_random_pointer_v1(self):
        # Create sample input
        node1 = RandomListNode(1)
        node2 = RandomListNode(2)
        node3 = RandomListNode(3)
        node1.next = node2
        node1.random = node3
        node2.next = node3
        node2.random = node1
        node3.next = None
        node3.random = node2
        
        # Call the function
        result = copy_random_pointer_v1(node1)
        
        # Assert statements
        self.assertEqual(result.label, 1)
        self.assertEqual(result.next.label, 2)
        self.assertEqual(result.random.label, 3)
        # Add more assertions as needed...

    def test_copy_random_pointer_v2(self):
        # Create sample input
        node1 = RandomListNode(1)
        node2 = RandomListNode(2)
        node3 = RandomListNode(3)
        node1.next = node2
        node1.random = node3
        node2.next = node3
        node2.random = node1
        node3.next = None
        node3.random = node2
        
        # Call the function
        result = copy_random_pointer_v2(node1)
        
        # Assert statements
        self.assertEqual(result.label, 1)
        self.assertEqual(result.next.label, 2)
        self.assertEqual(result.random.label, 3)
        # Add more assertions as needed...

if __name__ == '__main__':
    unittest.main()
