"""
Given a linked list, is_sort function returns true if the list is in sorted
(increasing) order and return false otherwise. An empty list is considered
to be sorted.

For example:
Null :List is sorted
1 2 3 4 :List is sorted
1 2 -1 3 :List is not sorted
"""


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

def is_sorted(head):
    if not head:
        return True
    current = head
    while current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True
