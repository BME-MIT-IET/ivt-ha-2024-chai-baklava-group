"""
Module containing classes for singly and doubly linked lists.
"""

class DoublyLinkedListNode:
    """
    Node class for a doubly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SinglyLinkedListNode:
    """
    Node class for a singly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
