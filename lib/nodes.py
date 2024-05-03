#!/usr/bin/python3.11.8

class InvertedIndexNodes(object):
    """
    `A simple class for abstracting nodes in linked list.`
    `docId`: gets an integer value for document id.
    `next`: gets the next node for pointing.
    """    
    __slots__ = ('docId', 'next')
    def __init__(self, docId: int, next=None) -> None:
        self.docId = docId
        self.next  = next
        