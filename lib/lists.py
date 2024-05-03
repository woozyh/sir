#!/usr/bin/python3.11.8

from nodes import InvertedIndexNodes

class InvertedList(object):

    """
    A simple linked list implementation with 3 parameter:
        `head`: always points to first node of list.
        `tail`: always points to last node of list.
        `size`: for each item it stores the size that item.(size -> length)
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def addToTail(self, docId: int) -> None:
        newDoc = InvertedIndexNodes(docId)
        if (self.isEmpty()):
            self.head = self.tail = newDoc
        else: 
            self.tail.next = newDoc
            self.tail = newDoc
        self.size += 1

